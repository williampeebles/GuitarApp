import unittest
from unittest.mock import patch

from maintenanceController import MaintenanceController


class TestMaintenanceController(unittest.TestCase):
    def setUp(self):
        self.db_patcher = patch("maintenanceController.DatabaseController")
        self.mock_db_class = self.db_patcher.start()
        self.addCleanup(self.db_patcher.stop)

        self.mock_db = self.mock_db_class.return_value
        self.mock_db.get_category_by_name.return_value = None
        self.mock_db.get_elements_by_category.return_value = []

    def create_controller(self):
        return MaintenanceController()

    def test_loads_completed_lessons_from_database(self):
        self.mock_db.get_category_by_name.return_value = {"category_id": 12}
        self.mock_db.get_elements_by_category.return_value = [
            {"element_type": "String Cleaning", "completed": 1},
            {"element_type": "Neck Check", "completed": 0},
            {"element_type": "Fret Polish", "completed": True},
        ]

        controller = self.create_controller()

        self.assertEqual(controller.category_id, 12)
        self.assertEqual(controller.completed_lessons, {"String Cleaning", "Fret Polish"})

    def test_get_lesson_content_for_missing_lesson_returns_placeholder(self):
        controller = self.create_controller()

        content = controller.get_lesson_content("Missing Lesson")

        self.assertIn("Content for Missing Lesson", content)
        self.assertIn("will be added soon", content)

    def test_start_quiz_for_current_requires_topic_and_lesson(self):
        controller = self.create_controller()

        questions = controller.start_quiz_for_current()

        self.assertEqual(questions, [])
        self.assertEqual(controller.last_quiz_questions, [])

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

    def test_submit_quiz_answers_marks_lesson_completed_on_pass(self):
        self.mock_db.get_category_by_name.return_value = {"category_id": 20}
        controller = self.create_controller()
        controller.current_topic = "Maintenance Basics"
        controller.current_lesson = "String Care"
        controller.last_quiz_questions = [
            {"answer": 0},
            {"answer": 1},
            {"answer": 2},
            {"answer": 3},
            {"answer": 0},
        ]

        result = controller.submit_quiz_answers([0, 1, 2, 3, 1])

        self.assertTrue(result["passed"])
        self.assertTrue(result["completed_now"])
        self.mock_db.mark_element_completed.assert_called_once_with(20, "String Care", completed=1)
        self.assertIn("String Care", controller.completed_lessons)

    def test_submit_quiz_answers_does_not_mark_completed_on_fail(self):
        self.mock_db.get_category_by_name.return_value = {"category_id": 21}
        controller = self.create_controller()
        controller.current_topic = "Maintenance Basics"
        controller.current_lesson = "String Care"
        controller.last_quiz_questions = [
            {"answer": 0},
            {"answer": 1},
            {"answer": 2},
            {"answer": 3},
            {"answer": 0},
        ]

        result = controller.submit_quiz_answers([0, 1, 9, 9, 9])

        self.assertFalse(result["passed"])
        self.assertIn("You need 4/5", result["message"])
        self.mock_db.mark_element_completed.assert_not_called()

    def test_close_closes_database_controller(self):
        controller = self.create_controller()

        controller.close()

        self.mock_db.close.assert_called_once()


if __name__ == "__main__":
    unittest.main()
