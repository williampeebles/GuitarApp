import unittest
from unittest.mock import Mock, patch

from tabController import TabController


class TestTabController(unittest.TestCase):
    @patch("tabController.MaintenanceTab")
    @patch("tabController.SongsTab")
    @patch("tabController.ChordsTab")
    @patch("tabController.FundamentalsTab")
    @patch("tabController.DashboardTab")
    @patch("tabController.ttk.Notebook")
    @patch("tabController.ttk.Style")
    def test_create_tabs_adds_all_tabs_in_order(
        self,
        mock_style,
        mock_notebook,
        mock_dashboard_tab,
        mock_fundamentals_tab,
        mock_chords_tab,
        mock_songs_tab,
        mock_maintenance_tab,
    ):
        notebook_instance = Mock()
        mock_notebook.return_value = notebook_instance

        mock_dashboard_tab.return_value = Mock(frame="dashboard-frame")
        mock_fundamentals_tab.return_value = Mock(frame="fundamentals-frame")
        mock_chords_tab.return_value = Mock(frame="chords-frame")
        mock_songs_tab.return_value = Mock(frame="songs-frame")
        mock_maintenance_tab.return_value = Mock(frame="maintenance-frame")

        controller = TabController(parent=Mock())

        self.assertIsNotNone(controller.get_notebook())
        self.assertEqual(notebook_instance.add.call_count, 5)

        added_tab_labels = [call.kwargs["text"] for call in notebook_instance.add.call_args_list]
        self.assertEqual(
            added_tab_labels,
            ["Dashboard", "Fundamentals", "Chords", "Songs", "Maintenance"],
        )

        mock_style.assert_called_once()

    @patch("tabController.MaintenanceTab")
    @patch("tabController.SongsTab")
    @patch("tabController.ChordsTab")
    @patch("tabController.FundamentalsTab")
    @patch("tabController.DashboardTab")
    @patch("tabController.ttk.Notebook")
    @patch("tabController.ttk.Style")
    def test_close_calls_close_on_supported_tabs(
        self,
        _mock_style,
        mock_notebook,
        mock_dashboard_tab,
        mock_fundamentals_tab,
        mock_chords_tab,
        mock_songs_tab,
        mock_maintenance_tab,
    ):
        mock_notebook.return_value = Mock()

        dashboard_instance = Mock(frame="dashboard-frame")
        fundamentals_instance = Mock(frame="fundamentals-frame")
        chords_instance = Mock(frame="chords-frame")
        songs_instance = Mock(frame="songs-frame")
        maintenance_instance = Mock(frame="maintenance-frame")

        mock_dashboard_tab.return_value = dashboard_instance
        mock_fundamentals_tab.return_value = fundamentals_instance
        mock_chords_tab.return_value = chords_instance
        mock_songs_tab.return_value = songs_instance
        mock_maintenance_tab.return_value = maintenance_instance

        controller = TabController(parent=Mock())
        controller.close()

        dashboard_instance.close.assert_called_once()
        fundamentals_instance.close.assert_called_once()
        chords_instance.close.assert_called_once()
        maintenance_instance.close.assert_called_once()
        songs_instance.close.assert_not_called()


if __name__ == "__main__":
    unittest.main()
