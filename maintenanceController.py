from maintenanceContent import MaintenanceContent
from databaseController import DatabaseController


class MaintenanceController:
    """Provides maintenance lesson data and selection state."""

    def __init__(self):
        self.db = DatabaseController()
        self.category_id = None
        self.lesson_items_by_topic = MaintenanceContent.LESSON_ITEMS_BY_TOPIC
        self.lesson_content = MaintenanceContent.LESSON_CONTENT
        self.quiz_bank_by_lesson = MaintenanceContent.QUIZ_BANK_BY_LESSON
        self.quiz_bank_by_topic = MaintenanceContent.QUIZ_BANK_BY_TOPIC
        self.completed_lessons = set()
        self.current_topic = None
        self.current_lesson = None
        self.last_quiz_questions = []
        self._load_completed_lessons()

    def _load_completed_lessons(self):
        category = self.db.get_category_by_name("Maintenance")
        if not category:
            return

        self.category_id = category["category_id"]
        elements = self.db.get_elements_by_category(self.category_id)
        self.completed_lessons = {
            element["element_type"]
            for element in elements
            if element.get("completed")
        }

    def get_all_topics(self):
        return list(self.lesson_items_by_topic.keys())

    def get_lessons_for_topic(self, topic_name):
        return list(self.lesson_items_by_topic.get(topic_name, []))

    def set_topic(self, topic_name):
        self.current_topic = topic_name

    def set_lesson(self, lesson_name):
        self.current_lesson = lesson_name
        self.last_quiz_questions = []

    def get_lesson_content(self, lesson_name):
        return self.lesson_content.get(
            lesson_name,
            f"Content for {lesson_name}\\n\\nThis lesson content will be added soon.",
        )

    def get_current_lesson(self):
        return self.current_lesson

    def is_lesson_completed(self, lesson_name):
        return lesson_name in self.completed_lessons

    def get_lesson_button_text(self, lesson_name):
        if self.is_lesson_completed(lesson_name):
            return f"{lesson_name} [Completed]"
        return lesson_name

    def get_quiz_questions(self, lesson_name, topic_name):
        questions = list(self.quiz_bank_by_lesson.get(lesson_name, []))
        if not questions:
            questions = list(self.quiz_bank_by_topic.get(topic_name, []))
        if len(questions) < 5:
            questions.extend(MaintenanceContent.EXTRA_QUIZ_QUESTIONS)
        return questions[:5]

    def start_quiz_for_current(self):
        if not self.current_lesson or not self.current_topic:
            self.last_quiz_questions = []
            return []

        self.last_quiz_questions = self.get_quiz_questions(self.current_lesson, self.current_topic)
        return list(self.last_quiz_questions)

    def submit_quiz_answers(self, selected_indexes):
        if not self.last_quiz_questions:
            return {
                "passed": False,
                "message": "",
                "correct": 0,
                "total": 0,
                "completed_now": False,
            }

        if any(choice == -1 for choice in selected_indexes):
            return {
                "passed": False,
                "message": "Please answer all five questions before submitting.",
                "correct": 0,
                "total": len(self.last_quiz_questions),
                "completed_now": False,
            }

        correct_count = 0
        for question, choice in zip(self.last_quiz_questions, selected_indexes):
            if choice == question["answer"]:
                correct_count += 1

        total = len(self.last_quiz_questions)
        passed = correct_count >= 4
        completed_now = False
        if passed and self.current_lesson:
            completed_now = self.current_lesson not in self.completed_lessons
            self.mark_lesson_completed(self.current_lesson)

        message = (
            f"Score: {correct_count}/{total}. Lesson marked as completed."
            if passed
            else f"Score: {correct_count}/{total}. You need 4/5 to complete. Try again."
        )

        return {
            "passed": passed,
            "message": message,
            "correct": correct_count,
            "total": total,
            "completed_now": completed_now,
        }

    def mark_lesson_completed(self, lesson_name):
        if self.category_id is None:
            return

        self.db.mark_element_completed(self.category_id, lesson_name, completed=1)
        self.completed_lessons.add(lesson_name)

    def close(self):
        if self.db:
            self.db.close()
