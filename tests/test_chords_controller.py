import unittest
from unittest.mock import patch

from chordsController import ChordsController


class TestChordsController(unittest.TestCase):
    def setUp(self):
        self.db_patcher = patch("chordsController.DatabaseController")
        self.formatter_patcher = patch("chordsController.ChordInfoFormatter.build_info_text")
        self.mock_db_class = self.db_patcher.start()
        self.mock_formatter = self.formatter_patcher.start()
        self.addCleanup(self.db_patcher.stop)
        self.addCleanup(self.formatter_patcher.stop)

        self.mock_db = self.mock_db_class.return_value
        self.mock_db.get_category_by_name.return_value = None
        self.mock_db.get_elements_by_category.return_value = []
        self.mock_formatter.return_value = "Formatted chord info"

    def create_controller(self):
        return ChordsController()

    def test_loads_mastered_chords_from_database(self):
        self.mock_db.get_category_by_name.return_value = {"category_id": 5}
        self.mock_db.get_elements_by_category.return_value = [
            {"element_type": "A", "completed": 1},
            {"element_type": "B", "completed": 0},
            {"element_type": "C", "completed": True},
        ]

        controller = self.create_controller()

        self.assertEqual(controller.category_id, 5)
        self.assertEqual(controller.mastered_chords, {"A", "C"})

    def test_set_chord_mastered_updates_database_and_cache(self):
        self.mock_db.get_category_by_name.return_value = {"category_id": 7}
        controller = self.create_controller()

        chord_name = controller.chord_names[0]
        controller.set_chord_mastered(chord_name, mastered=True)

        self.mock_db.mark_element_completed.assert_called_once_with(7, chord_name, completed=1)
        self.assertIn(chord_name, controller.mastered_chords)

    def test_unset_chord_mastered_updates_database_and_cache(self):
        self.mock_db.get_category_by_name.return_value = {"category_id": 9}
        self.mock_db.get_elements_by_category.return_value = [{"element_type": "A", "completed": 1}]
        controller = self.create_controller()

        controller.set_chord_mastered("A", mastered=False)

        self.mock_db.mark_element_completed.assert_called_once_with(9, "A", completed=0)
        self.assertNotIn("A", controller.mastered_chords)

    def test_set_chord_mastered_noop_when_category_missing(self):
        controller = self.create_controller()

        controller.set_chord_mastered("A", mastered=True)

        self.mock_db.mark_element_completed.assert_not_called()

    def test_get_chord_details_returns_none_for_unknown(self):
        controller = self.create_controller()

        details = controller.get_chord_details("NotAChord")

        self.assertIsNone(details)

    def test_get_chord_details_includes_mastery_state(self):
        self.mock_db.get_category_by_name.return_value = {"category_id": 11}
        self.mock_db.get_elements_by_category.return_value = []
        controller = self.create_controller()
        chord_name = controller.chord_names[0]
        self.mock_db.get_elements_by_category.return_value = [{"element_type": chord_name, "completed": 1}]
        controller.mastered_chords = {chord_name}

        details = controller.get_chord_details(chord_name)

        self.assertIsNotNone(details)
        self.assertEqual(details["name"], chord_name)
        self.assertTrue(details["mastered"])
        self.assertIn("strings", details)
        self.assertIn("fingers", details)

    def test_get_chord_info_text_delegates_to_formatter(self):
        controller = self.create_controller()
        chord_details = {"name": "A"}

        text = controller.get_chord_info_text(chord_details)

        self.mock_formatter.assert_called_once_with(chord_details)
        self.assertEqual(text, "Formatted chord info")

    def test_close_closes_database_controller(self):
        controller = self.create_controller()

        controller.close()

        self.mock_db.close.assert_called_once()


if __name__ == "__main__":
    unittest.main()
