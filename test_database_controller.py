import os
import tempfile
import unittest

from database import Database
from databaseController import DatabaseController


class TestDatabaseController(unittest.TestCase):
    # Build a fresh temporary database for each test so tests do not affect each other.
    def setUp(self):
        temp = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
        self.db_path = temp.name
        temp.close()

        schema_db = Database(self.db_path)
        schema_db.create_schema()
        schema_db.close()

        self.controller = DatabaseController(self.db_path)

    # Close and delete the temporary database after each test.
    def tearDown(self):
        self.controller.close()
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    # Insert a category and verify it can be read by list and by name.
    def test_insert_and_read_category(self):
        self.controller.insert_category("Fundamentals")

        all_categories = self.controller.get_all_categories()
        self.assertEqual(len(all_categories), 1)
        self.assertEqual(all_categories[0]["name_text"], "Fundamentals")

        category = self.controller.get_category_by_name("Fundamentals")
        self.assertIsNotNone(category)
        self.assertEqual(category["name_text"], "Fundamentals")

    # Looking up a missing category ID should return None.
    def test_get_category_by_id_returns_none_for_missing_record(self):
        category = self.controller.get_category_by_id(999)
        self.assertIsNone(category)

    # Insert elements and verify they can be retrieved by category and element ID.
    def test_insert_and_read_elements(self):
        self.controller.insert_category("Fundamentals")
        category = self.controller.get_category_by_name("Fundamentals")
        category_id = category["category_id"]

        self.controller.insert_element(category_id, "Lesson 1", completed=0)
        self.controller.insert_element(category_id, "Lesson 2", completed=1)

        elements = self.controller.get_elements_by_category(category_id)
        self.assertEqual(len(elements), 2)
        self.assertEqual(elements[0]["element_type"], "Lesson 1")
        self.assertEqual(elements[1]["completed"], 1)

        element_id = elements[0]["element_id"]
        by_id = self.controller.get_element_by_id(element_id)
        self.assertIsNotNone(by_id)
        self.assertEqual(by_id["element_type"], "Lesson 1")

    # Marking one element completed should recalculate category progress fields.
    def test_mark_element_completed_updates_progress(self):
        self.controller.insert_category("Fundamentals")
        category = self.controller.get_category_by_name("Fundamentals")
        category_id = category["category_id"]

        self.controller.insert_element(category_id, "Lesson 1", completed=0)
        self.controller.insert_element(category_id, "Lesson 2", completed=0)

        self.controller.mark_element_completed(category_id, "Lesson 1", completed=1)

        updated_category = self.controller.get_category_by_id(category_id)
        self.assertEqual(updated_category["number_of_elements"], 2)
        self.assertEqual(updated_category["tutorials_completed"], 1)
        self.assertEqual(updated_category["tutorials_left"], 1)
        self.assertEqual(updated_category["completion_percentage"], 50.0)

    # Progress calculation should safely return zeros when no elements exist.
    def test_update_category_progress_handles_zero_elements(self):
        self.controller.insert_category("Fundamentals")
        category = self.controller.get_category_by_name("Fundamentals")
        category_id = category["category_id"]

        self.controller.update_category_progress(category_id)

        updated = self.controller.get_category_by_id(category_id)
        self.assertEqual(updated["number_of_elements"], 0)
        self.assertEqual(updated["tutorials_completed"], 0)
        self.assertEqual(updated["tutorials_left"], 0)
        self.assertEqual(updated["completion_percentage"], 0.0)

    # Seeding twice should only add new lessons and keep existing ones.
    def test_seed_initial_data_adds_only_missing_items(self):
        self.controller.seed_initial_data(
            category_names=["Fundamentals", "Songs"],
            fundamentals_lessons=["Lesson A", "Lesson B"],
        )

        self.controller.seed_initial_data(
            category_names=["Fundamentals", "Songs"],
            fundamentals_lessons=["Lesson A", "Lesson B", "Lesson C"],
        )

        fundamentals = self.controller.get_category_by_name("Fundamentals")
        self.assertIsNotNone(fundamentals)
        songs = self.controller.get_category_by_name("Songs")
        self.assertIsNotNone(songs)

        lessons = self.controller.get_elements_by_category(fundamentals["category_id"])
        lesson_names = {lesson["element_type"] for lesson in lessons}
        self.assertEqual(lesson_names, {"Lesson A", "Lesson B", "Lesson C"})

    # Current schema allows duplicate category names, so two inserts make two rows.
    def test_duplicate_category_name_creates_two_rows(self):
        self.controller.insert_category("Fundamentals")
        self.controller.insert_category("Fundamentals")

        all_categories = self.controller.get_all_categories()
        self.assertEqual(len(all_categories), 2)

    # Marking a non-existent element as completed should keep completed count at zero.
    def test_mark_completed_for_missing_element_keeps_counts_zero(self):
        self.controller.insert_category("Fundamentals")
        category = self.controller.get_category_by_name("Fundamentals")
        category_id = category["category_id"]

        self.controller.mark_element_completed(category_id, "Lesson Does Not Exist", completed=1)

        updated = self.controller.get_category_by_id(category_id)
        self.assertEqual(updated["tutorials_completed"], 0)


if __name__ == "__main__":
    unittest.main()
