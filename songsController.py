import webbrowser
from songsContent import SongsContent


class SongsController:
    """Handles Songs tab behavior and data access."""

    def __init__(self):
        # Keep a mutable in-memory list so users can add songs during runtime.
        self.song_tutorials = list(SongsContent.SONG_TUTORIALS)

    def get_background_image_path(self):
        return SongsContent.BACKGROUND_IMAGE_PATH

    def get_tab_title(self):
        return SongsContent.TAB_TITLE

    def get_list_title(self):
        return SongsContent.LIST_TITLE

    def get_empty_state_text(self):
        return SongsContent.EMPTY_STATE_TEXT

    def get_song_tutorials(self):
        return list(self.song_tutorials)

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

        title = f"{song_name} - {author_name}"
        self.song_tutorials.append((title, url))
        return {
            "success": True,
            "message": "Song tutorial added.",
            "song": (title, url),
        }

    def open_song_link(self, url):
        webbrowser.open_new(url)
