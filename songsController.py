import webbrowser
from songsContent import SongsContent
from databaseController import DatabaseController


class SongsController:
    """Handles Songs tab behavior and data access."""

    def __init__(self, database_path=None):
        self.db = DatabaseController(database_path)
        self._remove_legacy_preloaded_songs()

    def _remove_legacy_preloaded_songs(self):
        """Remove legacy preloaded songs so the list starts user-defined only."""
        for title, url in SongsContent.LEGACY_PRELOADED_SONG_TUTORIALS:
            self.db.delete_song_tutorial(title, url)

    def get_background_image_path(self):
        return SongsContent.BACKGROUND_IMAGE_PATH

    def get_tab_title(self):
        return SongsContent.TAB_TITLE

    def get_list_title(self):
        return SongsContent.LIST_TITLE

    def get_empty_state_text(self):
        return SongsContent.EMPTY_STATE_TEXT

    def get_song_tutorials(self):
        tutorials = []
        for item in self.db.get_song_tutorials():
            title_text = item.get("title_text", "")
            artist_name = item.get("artist_name", "")
            url_text = item.get("url_text", "")
            display_title = f"{title_text} - {artist_name}" if artist_name else title_text
            tutorials.append((display_title, url_text))
        return tutorials

    def add_song_tutorial(self, song_name, author_name, url):
        song_name = (song_name or "").strip()
        author_name = (author_name or "").strip()
        url = (url or "").strip()

        if not song_name:
            return {
                "success": False,
                "message": "Please enter a song name.",
            }
        if not author_name:
            return {
                "success": False,
                "message": "Please enter an author name.",
            }
        if not (url.startswith("http://") or url.startswith("https://")):
            return {
                "success": False,
                "message": "Please enter a valid URL starting with http:// or https://.",
            }

        self.db.insert_song_tutorial(song_name, url, artist_name=author_name)
        title = f"{song_name} - {author_name}"
        return {
            "success": True,
            "message": "Song tutorial added.",
            "song": (title, url),
        }

    def open_song_link(self, url):
        webbrowser.open_new(url)

    def close(self):
        if self.db:
            self.db.close()
