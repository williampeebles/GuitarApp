import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from dashboardController import DashboardController


class DashboardTab:
    """
    Dashboard tab layout with a progress panel on the left and
    suggestions/achievements stacked on the right, plus a center content area.
    """

    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg="#f5f5f5")
        self.controller = DashboardController()
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

        progress_bar_container = tk.Frame(self.frame, height=70)
        progress_bar_container.pack(side=tk.TOP, fill=tk.X, padx=10, pady=(10, 0))
        progress_bar_container.pack_propagate(False)

        progress_canvas = tk.Canvas(progress_bar_container, height=70, highlightthickness=0, bd=0)
        progress_canvas.pack(fill=tk.BOTH, expand=True)

        progress_strip = ImageTk.PhotoImage(bg_image.crop((0, 0, WIDTH, 70)))
        progress_canvas.progress_strip = progress_strip
        progress_canvas.create_image(0, 0, image=progress_strip, anchor="nw")

        rank_progress = self.controller.get_rank_progress()

        dashboard_progress = ttk.Progressbar(
            progress_canvas,
            orient=tk.HORIZONTAL,
            length=400,
            mode="determinate",
        )
        dashboard_progress["value"] = rank_progress["progress_percent"]
        level_text_id = progress_canvas.create_text(
            0,
            10,
            text=rank_progress["current_rank"],
            font=("Arial", 12, "bold"),
            fill="#000000",
            anchor="n",
        )
        progress_window_id = progress_canvas.create_window(0, 34, anchor="n", window=dashboard_progress)

        progress_meta_id = progress_canvas.create_text(
            0,
            56,
            text=f"XP: {rank_progress['total_xp']}  •  Next: {rank_progress['next_rank']} ({rank_progress['xp_to_next']} XP)",
            font=("Arial", 10),
            fill="#000000",
            anchor="n",
        )

        def _center_progress_widgets(event):
            center_x = event.width / 2
            progress_canvas.coords(level_text_id, center_x, 10)
            progress_canvas.coords(progress_window_id, center_x, 34)
            progress_canvas.coords(progress_meta_id, center_x, 56)

        progress_canvas.bind("<Configure>", _center_progress_widgets)

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

        progress_breakdown_container = tk.Frame(progress_frame, bg="#000000")
        progress_breakdown_container.pack(fill=tk.BOTH, expand=True, padx=12, pady=(0, 12))

        progress_breakdown = self.controller.get_progress_breakdown()
        for section in progress_breakdown:
            section_row = tk.Frame(progress_breakdown_container, bg="#000000")
            section_row.pack(fill=tk.X, pady=(4, 0))

            section_label = tk.Label(
                section_row,
                text=f"{section['name']}: {section['percent']:.1f}%",
                font=("Arial", 11, "bold"),
                bg="#000000",
                fg="white",
                anchor="w",
                justify="left",
            )
            section_label.pack(side=tk.LEFT, fill=tk.X, expand=True)

            section_progress = ttk.Progressbar(
                section_row,
                orient=tk.HORIZONTAL,
                mode="determinate",
                length=300,
            )
            section_progress["value"] = section["percent"]
            section_progress.pack(side=tk.RIGHT, padx=(8, 0))

            for subsection in section.get("subsections", []):
                subsection_row = tk.Frame(progress_breakdown_container, bg="#000000")
                subsection_row.pack(fill=tk.X)

                subsection_label = tk.Label(
                    subsection_row,
                    text=f"  • {subsection['name']}: {subsection['percent']:.1f}%",
                    font=("Arial", 10),
                    bg="#000000",
                    fg="#d9d9d9",
                    anchor="w",
                    justify="left",
                    wraplength=340,
                )
                subsection_label.pack(side=tk.LEFT, fill=tk.X, expand=True)

                subsection_progress = ttk.Progressbar(
                    subsection_row,
                    orient=tk.HORIZONTAL,
                    mode="determinate",
                    length=260,
                )
                subsection_progress["value"] = subsection["percent"]
                subsection_progress.pack(side=tk.RIGHT, padx=(8, 0))

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

        suggestions_list_frame = tk.Frame(suggestions_frame, bg="#000000")
        suggestions_list_frame.pack(fill=tk.BOTH, expand=True, padx=12, pady=(0, 10))

        suggested_sections = self.controller.get_suggested_sections(limit=6)
        if not suggested_sections:
            no_suggestions_label = tk.Label(
                suggestions_list_frame,
                text="All tracked sections are complete.",
                font=("Arial", 10),
                bg="#000000",
                fg="#d9d9d9",
                anchor="w",
                justify="left",
            )
            no_suggestions_label.pack(fill=tk.X)
        else:
            for item in suggested_sections:
                suggestion_item_label = tk.Label(
                    suggestions_list_frame,
                    text=f"• {item['name']} ({item['percent']:.1f}%)",
                    font=("Arial", 10),
                    bg="#000000",
                    fg="#d9d9d9",
                    anchor="w",
                    justify="left",
                    wraplength=360,
                )
                suggestion_item_label.pack(fill=tk.X, pady=(0, 3))

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

    def close(self):
        if self.controller:
            self.controller.close()
