import unittest
from unittest.mock import patch

from dashboardController import DashboardController


class TestDashboardController(unittest.TestCase):
    def setUp(self):
        self.db_patcher = patch("dashboardController.DatabaseController")
        self.total_xp_patcher = patch("dashboardController.RankSystem.get_total_xp")
        self.rank_progress_patcher = patch("dashboardController.RankSystem.get_rank_progress_from_xp")
        self.breakdown_patcher = patch("dashboardController.ProgressBreakdown.build")

        self.mock_db_class = self.db_patcher.start()
        self.mock_total_xp = self.total_xp_patcher.start()
        self.mock_rank_progress = self.rank_progress_patcher.start()
        self.mock_breakdown = self.breakdown_patcher.start()

        self.addCleanup(self.db_patcher.stop)
        self.addCleanup(self.total_xp_patcher.stop)
        self.addCleanup(self.rank_progress_patcher.stop)
        self.addCleanup(self.breakdown_patcher.stop)

        self.mock_db = self.mock_db_class.return_value

    def create_controller(self):
        return DashboardController()

    def test_get_rank_progress_aggregates_counts_and_rank_data(self):
        category_map = {
            "Fundamentals": {"category_id": 1},
            "Maintenance": {"category_id": 2},
            "Chords": {"category_id": 3},
        }
        elements_map = {
            1: [{"completed": 1}, {"completed": 0}, {"completed": True}],
            2: [{"completed": 1}],
            3: [{"completed": 1}, {"completed": 1}, {"completed": 0}],
        }

        self.mock_db.get_category_by_name.side_effect = lambda name: category_map.get(name)
        self.mock_db.get_elements_by_category.side_effect = lambda category_id: elements_map.get(category_id, [])

        self.mock_total_xp.return_value = 123
        self.mock_rank_progress.return_value = {
            "current_rank": "Novice",
            "next_rank": "Apprentice",
            "progress_percent": 55.5,
            "xp_to_next": 40,
        }

        controller = self.create_controller()
        result = controller.get_rank_progress()

        self.mock_total_xp.assert_called_once_with(3, 2)
        self.mock_rank_progress.assert_called_once_with(123)
        self.assertEqual(result["completed_fundamentals"], 2)
        self.assertEqual(result["completed_maintenance"], 1)
        self.assertEqual(result["mastered_chords"], 2)
        self.assertEqual(result["current_rank"], "Novice")

    def test_get_progress_breakdown_passes_completed_sets_and_songs_percent(self):
        category_map = {
            "Fundamentals": {"category_id": 10},
            "Chords": {"category_id": 20},
            "Maintenance": {"category_id": 30},
            "Songs": {"category_id": 40, "completion_percentage": 33.3},
        }
        elements_map = {
            10: [{"element_type": "F1", "completed": 1}, {"element_type": "F2", "completed": 0}],
            20: [{"element_type": "A", "completed": 1}, {"element_type": "B", "completed": 1}],
            30: [{"element_type": "M1", "completed": 0}, {"element_type": "M2", "completed": True}],
        }

        self.mock_db.get_category_by_name.side_effect = lambda name: category_map.get(name)
        self.mock_db.get_elements_by_category.side_effect = lambda category_id: elements_map.get(category_id, [])
        self.mock_breakdown.return_value = [{"name": "Fundamentals", "percent": 10.0, "subsections": []}]

        controller = self.create_controller()
        result = controller.get_progress_breakdown()

        self.mock_breakdown.assert_called_once_with(
            fundamentals_completed={"F1"},
            chords_completed={"A", "B"},
            maintenance_completed={"M2"},
            songs_percent=33.3,
        )
        self.assertEqual(result, [{"name": "Fundamentals", "percent": 10.0, "subsections": []}])

    def test_get_suggested_sections_sorts_and_limits_results(self):
        controller = self.create_controller()
        controller.get_progress_breakdown = lambda: [
            {
                "name": "Chords",
                "percent": 40.0,
                "subsections": [
                    {"name": "Advanced Chords", "percent": 20.0},
                    {"name": "Beginner Chords", "percent": 20.0},
                ],
            },
            {
                "name": "Fundamentals",
                "percent": 80.0,
                "subsections": [{"name": "Posture", "percent": 10.0}],
            },
            {
                "name": "Songs",
                "percent": 70.0,
                "subsections": [],
            },
        ]

        suggestions = controller.get_suggested_sections(limit=3)

        self.assertEqual(len(suggestions), 3)
        self.assertEqual(suggestions[0]["name"], "Fundamentals • Posture")
        self.assertEqual(suggestions[1]["name"], "Chords • Beginner Chords")
        self.assertEqual(suggestions[2]["name"], "Chords • Advanced Chords")

    def test_close_calls_database_close(self):
        controller = self.create_controller()

        controller.close()

        self.mock_db.close.assert_called_once()


if __name__ == "__main__":
    unittest.main()
