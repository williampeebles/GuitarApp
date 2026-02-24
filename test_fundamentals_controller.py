import unittest
from unittest.mock import patch

from fundamentalsController import FundamentalsController


class TestFundamentalsController(unittest.TestCase):
    # Create a mocked database so tests stay fast and independent from real DB data.
    def setUp(self):
        self.db_patcher = patch("fundamentalsController.DatabaseController")
        self.mock_db_class = self.db_patcher.start()
        self.addCleanup(self.db_patcher.stop)

        self.mock_db = self.mock_db_class.return_value
        self.mock_db.get_category_by_name.return_value = None
        self.mock_db.get_elements_by_category.return_value = []

    def create_controller(self):
        return FundamentalsController()

    # Verify completed lessons are loaded from the database at startup.
    def test_loads_completed_lessons_from_database(self):
        self.mock_db.get_category_by_name.return_value = {"category_id": 42}
        self.mock_db.get_elements_by_category.return_value = [
            {"element_type": "Lesson A", "completed": 1},
            {"element_type": "Lesson B", "completed": 0},
            {"element_type": "Lesson C", "completed": True},
        ]

        controller = self.create_controller()

        self.assertEqual(controller.category_id, 42)
        self.assertEqual(controller.completed_lessons, {"Lesson A", "Lesson C"})

    # If a topic does not exist, the controller should return a safe default lesson.
    def test_get_lessons_for_unknown_topic_returns_fallback(self):
        controller = self.create_controller()

        lessons = controller.get_lessons_for_topic("Unknown Topic")

        self.assertEqual(lessons, ["Lesson 1: Introduction"])

    # Missing lesson content should return placeholder text instead of crashing.
    def test_get_lesson_content_for_missing_lesson_returns_placeholder(self):
        controller = self.create_controller()

        content = controller.get_lesson_content("Lesson That Does Not Exist")

        self.assertIn("Content for Lesson That Does Not Exist", content)
        self.assertIn("will be added soon", content)

    # Quiz generator should add extra questions when lesson/topic source has fewer than five.
    def test_get_quiz_questions_adds_extra_when_topic_has_too_few(self):
        controller = self.create_controller()
        controller.quiz_bank_by_lesson = {}
        controller.quiz_bank_by_topic = {
            "Tiny Topic": [
                {"question": "Q1", "choices": ["A"], "answer": 0},
                {"question": "Q2", "choices": ["A"], "answer": 0},
            ]
        }

        questions = controller.get_quiz_questions("Any Lesson", "Tiny Topic")

        self.assertEqual(len(questions), 4)
        self.assertEqual(questions[0]["question"], "Q1")
        self.assertEqual(questions[1]["question"], "Q2")

    # Quiz questions should come from the selected lesson when lesson-specific bank exists.
    def test_get_quiz_questions_prioritizes_lesson_specific_questions(self):
        controller = self.create_controller()
        controller.quiz_bank_by_lesson = {
            "Lesson A": [
                {"question": "Lesson A Q1", "choices": ["A"], "answer": 0},
                {"question": "Lesson A Q2", "choices": ["A"], "answer": 0},
                {"question": "Lesson A Q3", "choices": ["A"], "answer": 0},
                {"question": "Lesson A Q4", "choices": ["A"], "answer": 0},
                {"question": "Lesson A Q5", "choices": ["A"], "answer": 0},
            ]
        }
        controller.quiz_bank_by_topic = {
            "Topic X": [
                {"question": "Topic Q1", "choices": ["A"], "answer": 0},
                {"question": "Topic Q2", "choices": ["A"], "answer": 0},
                {"question": "Topic Q3", "choices": ["A"], "answer": 0},
                {"question": "Topic Q4", "choices": ["A"], "answer": 0},
                {"question": "Topic Q5", "choices": ["A"], "answer": 0},
            ]
        }

        questions = controller.get_quiz_questions("Lesson A", "Topic X")

        self.assertEqual(len(questions), 5)
        self.assertTrue(all(question["question"].startswith("Lesson A") for question in questions))

    # Completing a lesson should update both the DB and in-memory completed set.
    def test_mark_lesson_completed_updates_db_and_cache(self):
        self.mock_db.get_category_by_name.return_value = {"category_id": 7}
        controller = self.create_controller()

        controller.mark_lesson_completed("Lesson 2: Sitting Position")

        self.mock_db.mark_element_completed.assert_called_once_with(
            7, "Lesson 2: Sitting Position", completed=1
        )
        self.assertIn("Lesson 2: Sitting Position", controller.completed_lessons)

    # Quiz cannot start unless both a topic and a lesson are selected.
    def test_start_quiz_for_current_requires_topic_and_lesson(self):
        controller = self.create_controller()

        questions = controller.start_quiz_for_current()

        self.assertEqual(questions, [])
        self.assertEqual(controller.last_quiz_questions, [])

    # Submitting with unanswered questions should return a helpful warning message.
    def test_submit_quiz_answers_with_unanswered_question_returns_warning(self):
        controller = self.create_controller()
        controller.last_quiz_questions = [
            {"answer": 0},
            {"answer": 1},
            {"answer": 2},
            {"answer": 3},
            {"answer": 0},
        ]

        result = controller.submit_quiz_answers([0, 1, -1, 3, 0])

        self.assertFalse(result["passed"])
        self.assertIn("Please answer all five questions", result["message"])
        self.assertEqual(result["total"], 5)

    # Scoring 4/5 should pass and mark the current lesson as completed.
    def test_submit_quiz_answers_marks_lesson_completed_on_pass(self):
        self.mock_db.get_category_by_name.return_value = {"category_id": 9}
        controller = self.create_controller()
        controller.current_lesson = "Lesson 1: Body Posture"
        controller.last_quiz_questions = [
            {"answer": 0},
            {"answer": 1},
            {"answer": 2},
            {"answer": 3},
            {"answer": 0},
        ]

        result = controller.submit_quiz_answers([0, 1, 2, 3, 1])

        self.assertTrue(result["passed"])
        self.assertEqual(result["correct"], 4)
        self.assertTrue(result["completed_now"])
        self.mock_db.mark_element_completed.assert_called_once_with(
            9, "Lesson 1: Body Posture", completed=1
        )

    # If the score is too low, the lesson should not be marked completed.
    def test_submit_quiz_answers_does_not_mark_completed_on_fail(self):
        self.mock_db.get_category_by_name.return_value = {"category_id": 11}
        controller = self.create_controller()
        controller.current_lesson = "Lesson 1: Body Posture"
        controller.last_quiz_questions = [
            {"answer": 0},
            {"answer": 1},
            {"answer": 2},
            {"answer": 3},
            {"answer": 0},
        ]

        result = controller.submit_quiz_answers([0, 1, 9, 9, 9])

        self.assertFalse(result["passed"])
        self.assertEqual(result["correct"], 2)
        self.assertIn("You need 4/5", result["message"])
        self.mock_db.mark_element_completed.assert_not_called()

    # Duplicate edge-case check for unknown topics using the default intro lesson.
    def test_unknown_topic_uses_intro_lesson_default(self):
        controller = self.create_controller()

        lessons = controller.get_lessons_for_topic("Unknown Topic")

        self.assertEqual(lessons, ["Lesson 1: Introduction"])

    # Confirm that exactly four correct answers are enough to pass the quiz.
    def test_quiz_passes_with_four_correct_answers(self):
        controller = self.create_controller()
        controller.current_lesson = "Lesson 1: Body Posture"
        controller.last_quiz_questions = [
            {"answer": 0},
            {"answer": 1},
            {"answer": 2},
            {"answer": 3},
            {"answer": 0},
        ]

        result = controller.submit_quiz_answers([0, 1, 2, 3, 1])
        self.assertTrue(result["passed"])


if __name__ == "__main__":
    unittest.main()
