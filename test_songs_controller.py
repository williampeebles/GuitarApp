import unittest
from unittest.mock import patch

from songsController import SongsController
from songsContent import SongsContent


class TestSongsController(unittest.TestCase):
    def setUp(self):
        self.controller = SongsController()

    def test_content_accessors_return_songs_content_values(self):
        self.assertEqual(self.controller.get_background_image_path(), SongsContent.BACKGROUND_IMAGE_PATH)
        self.assertEqual(self.controller.get_tab_title(), SongsContent.TAB_TITLE)
        self.assertEqual(self.controller.get_list_title(), SongsContent.LIST_TITLE)
        self.assertEqual(self.controller.get_empty_state_text(), SongsContent.EMPTY_STATE_TEXT)
        self.assertEqual(self.controller.get_song_tutorials(), SongsContent.SONG_TUTORIALS)

    @patch("songsController.webbrowser.open_new")
    def test_open_song_link_uses_default_browser(self, mock_open_new):
        url = "https://example.com/tutorial"

        self.controller.open_song_link(url)

        mock_open_new.assert_called_once_with(url)

    def test_add_song_tutorial_appends_song(self):
        original_count = len(self.controller.get_song_tutorials())

        result = self.controller.add_song_tutorial(
            song_name="My Song",
            author_name="Test Artist",
            url="https://example.com/my-song",
        )

        self.assertTrue(result["success"])
        self.assertEqual(len(self.controller.get_song_tutorials()), original_count + 1)
        self.assertEqual(self.controller.get_song_tutorials()[-1], ("My Song - Test Artist", "https://example.com/my-song"))

    def test_add_song_tutorial_rejects_invalid_url(self):
        result = self.controller.add_song_tutorial(
            song_name="My Song",
            author_name="Test Artist",
            url="example.com/no-scheme",
        )

        self.assertFalse(result["success"])
        self.assertIn("valid URL", result["message"])


if __name__ == "__main__":
    unittest.main()
