import tkinter as tk
from PIL import Image, ImageTk


class WoodBackgroundManager:
    """Applies and maintains a full-cover wooden background on a Tk frame."""

    def __init__(self, frame, image_name="wooden_bg.jpg", fallback_color="#f5f5f5"):
        self.frame = frame
        self.image_name = image_name
        self.fallback_color = fallback_color
        self.background_label = None
        self.background_source = None
        self.background_image = None

    def apply(self):
        try:
            self.background_source = Image.open(self.image_name)

            initial_width = max(self.frame.winfo_width(), 1500)
            initial_height = max(self.frame.winfo_height(), 800)
            initial_image = self._get_cover_cropped_image(initial_width, initial_height)
            self.background_image = ImageTk.PhotoImage(initial_image)

            self.background_label = self._create_or_update_label(self.background_image)
            self.frame.bind("<Configure>", self._update_background_image, add="+")
        except Exception:
            self.frame.configure(bg=self.fallback_color)

    def _create_or_update_label(self, image):
        if self.background_label and getattr(self.background_label, "winfo_exists", lambda: False)():
            self.background_label.configure(image=image)
            self.background_label.image = image
            self.background_label.lower()
            return self.background_label

        label = tk.Label(self.frame, image=image, bd=0)
        label.image = image
        label.place(x=0, y=0, relwidth=1, relheight=1)
        label.lower()
        return label

    def _update_background_image(self, event):
        if not self.background_source:
            return

        width = max(event.width, 1)
        height = max(event.height, 1)
        resized = self._get_cover_cropped_image(width, height)
        self.background_image = ImageTk.PhotoImage(resized)
        self.background_label = self._create_or_update_label(self.background_image)

    def _get_cover_cropped_image(self, target_width, target_height):
        source_width, source_height = self.background_source.size
        scale = max(target_width / source_width, target_height / source_height)
        resized_width = int(source_width * scale)
        resized_height = int(source_height * scale)

        resized_image = self.background_source.resize((resized_width, resized_height), Image.LANCZOS)

        left = max((resized_width - target_width) // 2, 0)
        top = max((resized_height - target_height) // 2, 0)
        right = left + target_width
        bottom = top + target_height

        return resized_image.crop((left, top, right, bottom))
