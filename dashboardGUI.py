import tkinter as tk
from PIL import Image, ImageTk


class DashboardTab:
    """
    Dashboard tab layout with a progress panel on the left and
    suggestions/achievements stacked on the right, plus a center content area.
    """

    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg="#f5f5f5")
        self._build_layout()

    def _build_layout(self):
        # Add background image
        IMAGE_PATH = 'wooden_bg.jpg'
        WIDTH, HEIGHT = 1500, 800
        bg_image = Image.open(IMAGE_PATH).resize((WIDTH, HEIGHT), Image.LANCZOS)
        img = ImageTk.PhotoImage(bg_image)
        lbl = tk.Label(self.frame, image=img)
        lbl.img = img  # Keep a reference in case this code put is in a function.
        lbl.place(relx=0.5, rely=0.5, anchor='center')  # Place label in center of parent.

        # Progress frame on the left
        progress_frame = tk.Frame(
            self.frame,
            bg="#000000",
            relief=tk.SUNKEN,
            bd=2,
            width=500,
        )
        progress_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=(10, 5), pady=10, expand=False)
        progress_frame.pack_propagate(False)

        progress_label = tk.Label(
            progress_frame,
            text="Progress",
            font=("Arial", 14),
            bg="#000000",
            fg="white",
        )
        progress_label.pack(pady=10)

        # Right side container for suggestions and achievements
        right_container = tk.Frame(self.frame, bg="#f5f5f5")
        right_container.pack(side=tk.RIGHT, fill=tk.BOTH, padx=(5, 10), pady=10, expand=False)

        # Suggestions frame on top
        suggestions_frame = tk.Frame(
            right_container,
            bg="#000000",
            relief=tk.SUNKEN,
            bd=2,
            width=400,
        )
        suggestions_frame.pack(side=tk.TOP, fill=tk.BOTH, pady=(0, 5), expand=True)
        suggestions_frame.pack_propagate(False)

        suggestions_label = tk.Label(
            suggestions_frame,
            text="Suggestions",
            font=("Arial", 14),
            bg="#000000",
            fg="white",
        )
        suggestions_label.pack(pady=10)

        # Achievements frame on bottom
        achievements_frame = tk.Frame(
            right_container,
            bg="#000000",
            relief=tk.SUNKEN,
            bd=2,
            width=400,
        )
        achievements_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        achievements_frame.pack_propagate(False)

        achievements_label = tk.Label(
            achievements_frame,
            text="Achievements",
            font=("Arial", 14),
            bg="#000000",
            fg="white",
        )
        achievements_label.pack(pady=10)

        # Center content area
        content_frame = tk.Frame(
            self.frame,
            bg="#ffffff",
            relief=tk.RIDGE,
            bd=2,
        )
        content_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=10)

        dashboard_title = tk.Label(
            content_frame,
            text="Dashboard",
            font=("Arial", 24),
            bg="#ffffff",
        )
        dashboard_title.pack(pady=20, padx=20)
