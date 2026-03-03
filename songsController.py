import webbrowser
from songsContent import SongsContent


class SongsController:
    """Handles Songs tab behavior and data access."""

    def get_background_image_path(self):
        return SongsContent.BACKGROUND_IMAGE_PATH

    def get_tab_title(self):
        return SongsContent.TAB_TITLE

    def get_list_title(self):
        return SongsContent.LIST_TITLE

    def get_empty_state_text(self):
        return SongsContent.EMPTY_STATE_TEXT

    def get_song_tutorials(self):
        return SongsContent.SONG_TUTORIALS

    def open_song_link(self, url):
        webbrowser.open_new(url)
