import webbrowser
from contentLoader import load_content_file
from databaseController import DatabaseController


class SongsController:
    """Handles Songs tab behavior and data access."""

    _content = None

    @classmethod
    def _get_content(cls):
        if cls._content is None:
            cls._content = load_content_file("songs_content.txt")
        return cls._content

    def __init__(self, database_path=None):
        self.db = DatabaseController(database_path)
        self.content = self._get_content()

    def get_background_image_path(self):
        return self.content["BACKGROUND_IMAGE_PATH"]

    def get_tab_title(self):
        return self.content["TAB_TITLE"]

    def get_list_title(self):
        return self.content["LIST_TITLE"]

    def get_empty_state_text(self):
        return self.content["EMPTY_STATE_TEXT"]

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
