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
        self.background_source = None
        self.background_image = None
        self.background_label = None
        self._build_layout()

    def _build_layout(self):
        # Add background image
        IMAGE_PATH = 'wooden_bg.jpg'
        self.background_source = Image.open(IMAGE_PATH)
        initial_bg = self.background_source.resize((1500, 800), Image.LANCZOS)
        self.background_image = ImageTk.PhotoImage(initial_bg)
        self.background_label = tk.Label(self.frame, image=self.background_image)
        self.background_label.img = self.background_image
        self.background_label.place(relx=0.5, rely=0.5, anchor='center')

        def _resize_background(_event=None):
            width = max(self.frame.winfo_width(), 1)
            height = max(self.frame.winfo_height(), 1)
            resized = self.background_source.resize((width, height), Image.LANCZOS)
            self.background_image = ImageTk.PhotoImage(resized)
            self.background_label.configure(image=self.background_image)
            self.background_label.img = self.background_image

        self.frame.bind("<Configure>", _resize_background, add="+")
        self.frame.after(0, _resize_background)

        progress_bar_container = tk.Frame(self.frame, height=70)
        progress_bar_container.pack(side=tk.TOP, fill=tk.X, padx=10, pady=(10, 0))
        progress_bar_container.pack_propagate(False)

        progress_canvas = tk.Canvas(progress_bar_container, height=70, highlightthickness=0, bd=0)
        progress_canvas.pack(fill=tk.BOTH, expand=True)

        strip_height = min(70, self.background_source.height)
        progress_strip_source = self.background_source.crop((0, 0, self.background_source.width, strip_height))
        progress_strip = ImageTk.PhotoImage(progress_strip_source.resize((1500, 70), Image.LANCZOS))
        progress_canvas.progress_strip = progress_strip
        progress_strip_id = progress_canvas.create_image(0, 0, image=progress_strip, anchor="nw")

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
            if event.width > 1 and event.height > 1:
                resized_strip = progress_strip_source.resize((event.width, event.height), Image.LANCZOS)
                progress_canvas.progress_strip = ImageTk.PhotoImage(resized_strip)
                progress_canvas.itemconfig(progress_strip_id, image=progress_canvas.progress_strip)
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
        progress_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=(10, 5), pady=10, expand=True)
        progress_frame.pack_propagate(False)

        progress_label = tk.Label(
            progress_frame,
            text="Progress",
            font=("Arial", 18, "bold"),
            bg="#000000",
            fg="white",
        )
        progress_label.pack(pady=10)

        progress_breakdown_container = tk.Frame(progress_frame, bg="#000000")
        progress_breakdown_container.pack(fill=tk.BOTH, expand=True, padx=12, pady=(0, 12))

        progress_breakdown = self.controller.get_progress_breakdown()
        for section in progress_breakdown:
            section_row = tk.Frame(progress_breakdown_container, bg="#000000", height=35)
            section_row.pack(fill=tk.X, pady=(8, 2))
            section_row.pack_propagate(False)

            section_label = tk.Label(
                section_row,
                text=f"{section['name']}: {section['percent']:.1f}%",
                font=("Arial", 13, "bold"),
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
                length=420,
            )
            section_progress["value"] = section["percent"]
            section_progress.pack(side=tk.RIGHT, padx=(8, 0))

            for subsection in section.get("subsections", []):
                subsection_row = tk.Frame(progress_breakdown_container, bg="#000000", height=28)
                subsection_row.pack(fill=tk.X, pady=(4, 0))
                subsection_row.pack_propagate(False)

                subsection_label = tk.Label(
                    subsection_row,
                    text=f"  • {subsection['name']}: {subsection['percent']:.1f}%",
                    font=("Arial", 12),
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
                    length=360,
                )
                subsection_progress["value"] = subsection["percent"]
                subsection_progress.pack(side=tk.RIGHT, padx=(8, 0))

        # Right side container for suggestions
        right_container = tk.Frame(self.frame, bg="#f5f5f5")
        right_container.pack(side=tk.RIGHT, fill=tk.BOTH, padx=(5, 10), pady=10, expand=False)

        # Suggestions frame
        suggestions_frame = tk.Frame(
            right_container,
            bg="#000000",
            relief=tk.SUNKEN,
            bd=2,
            width=400,
        )
        suggestions_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        suggestions_frame.pack_propagate(False)

        suggestions_label = tk.Label(
            suggestions_frame,
            text="Suggestions",
            font=("Arial", 18, "bold"),
            bg="#000000",
            fg="white",
        )
        suggestions_label.pack(pady=10)

        suggestions_list_frame = tk.Frame(suggestions_frame, bg="#000000")
        suggestions_list_frame.pack(fill=tk.BOTH, expand=True, padx=12, pady=(0, 10))

        suggested_sections = self.controller.get_suggested_sections(limit=7)
        if not suggested_sections:
            no_suggestions_label = tk.Label(
                suggestions_list_frame,
                text="All tracked sections are complete.",
                font=("Arial", 12),
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
                    font=("Arial", 12),
                    bg="#000000",
                    fg="#d9d9d9",
                    anchor="w",
                    justify="left",
                    wraplength=360,
                )
                suggestion_item_label.pack(fill=tk.X, pady=(0, 3))

    def close(self):
        if self.controller:
            self.controller.close()
