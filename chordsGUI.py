import tkinter as tk
import customtkinter as ctk
import os
from PIL import Image, ImageTk
from chordsController import ChordsController
from slide_panel import SlidePanel


class ChordsTab:
    """Chords tab with a slide-panel chord selector and detail panel."""

    def __init__(self, parent):
        self.controller = ChordsController()
        self.frame = tk.Frame(parent, bg="#f5f5f5")
        self.sidebar_panel = None
        self.background_image = None
        self.background_label = None
        self.background_source = None
        self.current_chord_name = self.controller.get_default_chord()
        self.header_title_var = tk.StringVar(value=self.controller.get_default_chord())
        self.chord_label_var = tk.StringVar(value="")
        self.mastery_status_var = tk.StringVar(value="")
        self.chord_info_var = tk.StringVar(value="")
        self.chord_canvas = None
        self.mastery_button = None
        self._build_layout()
        self._show_chord(self.controller.get_default_chord())

    def _build_layout(self):
        self._set_wood_background()

        # Content overlay frame on top of wooden background
        content_frame = tk.Frame(self.frame, bg="white", relief=tk.RIDGE, bd=1)
        content_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.82, relheight=0.9)

        header_frame = tk.Frame(content_frame, bg="white")
        header_frame.pack(fill="x", padx=12, pady=(12, 6))

        button_container = tk.Frame(header_frame, bg="white")
        button_container.pack(side=tk.LEFT)

        self.toggle_button = ctk.CTkButton(
            button_container,
            text="≡ Chords",
            font=("Arial", 14),
            width=110,
            fg_color="#333333",
            text_color="white",
            hover_color="#555555",
            command=self._toggle_sidebar,
        )
        self.toggle_button.pack(side=tk.LEFT)

        title = tk.Label(
            header_frame,
            textvariable=self.header_title_var,
            font=("Arial", 28, "bold"),
            bg="white",
            fg="#000000",
        )
        title.pack(side=tk.LEFT, padx=(20, 0))

        content_container = tk.Frame(content_frame, bg="white")
        content_container.pack(fill="both", expand=True, padx=12, pady=(0, 12))
        content_container.grid_rowconfigure(0, weight=1)
        content_container.grid_columnconfigure(0, weight=1)

        self._build_chord_detail(content_container)
        self._build_chord_sidebar(content_container)

    def _set_wood_background(self):
        try:
            image_path = os.path.join(os.path.dirname(__file__), "wooden_bg.jpg")
            self.background_source = Image.open(image_path)
            initial_image = self._get_cover_cropped_image(1500, 800)
            self.background_image = ImageTk.PhotoImage(initial_image)
            self.background_label = tk.Label(self.frame, image=self.background_image, bd=0)
            self.background_label.image = self.background_image
            self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
            self.background_label.lower()
            self.frame.bind("<Configure>", self._update_background_image)
        except Exception:
            self.frame.configure(bg="#f5f5f5")

    def _update_background_image(self, event):
        if not self.background_source or not self.background_label:
            return

        width = max(event.width, 1)
        height = max(event.height, 1)
        resized = self._get_cover_cropped_image(width, height)
        self.background_image = ImageTk.PhotoImage(resized)
        self.background_label.configure(image=self.background_image)
        self.background_label.image = self.background_image
        self.background_label.lower()

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

    def _build_chord_sidebar(self, parent):
        self.sidebar_panel = SlidePanel(parent, -0.35, 0.0)
        self.sidebar_panel.configure(fg_color="#2b2b2b")

        sidebar_title = ctk.CTkLabel(
            self.sidebar_panel,
            text="Chords",
            font=("Arial", 16, "bold"),
            text_color="white",
        )
        sidebar_title.pack(pady=10)

        scrollable_frame = ctk.CTkScrollableFrame(self.sidebar_panel, fg_color="#2b2b2b", label_text="")
        scrollable_frame.pack(fill="both", expand=True, padx=5, pady=5)

        for section in self.controller.get_category_layout():
            section_title = ctk.CTkLabel(
                scrollable_frame,
                text=section["title"],
                font=("Arial", 13, "bold"),
                text_color="white",
                anchor="w",
            )
            section_title.pack(fill="x", padx=5, pady=(10, 4))

            for group in section["groups"]:
                group_label = ctk.CTkLabel(
                    scrollable_frame,
                    text=group["label"],
                    font=("Arial", 11, "bold"),
                    text_color="#d9d9d9",
                    anchor="w",
                )
                group_label.pack(fill="x", padx=10, pady=(4, 2))

                if group["item_type"] == "chord":
                    for chord_name in group["items"]:
                        chord_btn = ctk.CTkButton(
                            scrollable_frame,
                            text=chord_name,
                            font=("Arial", 11),
                            fg_color="#404040",
                            text_color="white",
                            hover_color="#505050",
                            corner_radius=5,
                            command=lambda selected=chord_name: self._show_chord(selected),
                        )
                        chord_btn.pack(fill="x", padx=15, pady=3)
                else:
                    for progression in group["items"]:
                        progression_label = ctk.CTkLabel(
                            scrollable_frame,
                            text=f"• {progression}",
                            font=("Arial", 10),
                            text_color="#c8c8c8",
                            anchor="w",
                        )
                        progression_label.pack(fill="x", padx=20, pady=(0, 2))

    def _build_chord_detail(self, parent):
        main_content = tk.Frame(parent, bg="white", relief=tk.SUNKEN, bd=1)
        main_content.grid(row=0, column=0, sticky="nsew")

        detail_frame = tk.Frame(main_content, bg="white")
        detail_frame.pack(fill="both", expand=True, padx=12, pady=12)
        detail_frame.grid_rowconfigure(0, weight=1)
        detail_frame.grid_columnconfigure(0, weight=0)
        detail_frame.grid_columnconfigure(1, weight=1)

        info_section = tk.Frame(detail_frame, bg="white")
        info_section.grid(row=0, column=0, sticky="nsw", padx=(16, 12), pady=16)

        chord_sub_label = tk.Label(
            info_section,
            textvariable=self.chord_label_var,
            font=("Arial", 12),
            bg="white",
            fg="#4a4a4a",
            justify="left",
            wraplength=240,
        )
        chord_sub_label.pack(anchor="w", pady=(6, 0))

        mastery_status_label = tk.Label(
            info_section,
            textvariable=self.mastery_status_var,
            font=("Arial", 11, "bold"),
            bg="white",
            fg="#2f6f44",
            justify="left",
            wraplength=240,
        )
        mastery_status_label.pack(anchor="w", pady=(6, 0))

        self.mastery_button = ctk.CTkButton(
            info_section,
            text="Mark as Mastered",
            font=("Arial", 12),
            width=170,
            fg_color="#2f6f44",
            text_color="white",
            hover_color="#245837",
            command=self._toggle_mastery,
        )
        self.mastery_button.pack(anchor="w", pady=(8, 0))

        chord_info_label = tk.Label(
            info_section,
            textvariable=self.chord_info_var,
            font=("Arial", 12),
            bg="white",
            fg="#2f2f2f",
            justify="left",
            anchor="nw",
            wraplength=360,
        )
        chord_info_label.pack(anchor="w", pady=(12, 0), fill="x")

        diagram_section = tk.Frame(detail_frame, bg="white")
        diagram_section.grid(row=0, column=1, sticky="nsew", padx=(12, 16), pady=16)
        diagram_section.grid_rowconfigure(1, weight=1)
        diagram_section.grid_columnconfigure(0, weight=1)

        self.chord_canvas = tk.Canvas(
            diagram_section,
            width=360,
            height=420,
            bg="white",
            highlightthickness=1,
            highlightbackground="#d9d9d9",
        )
        self.chord_canvas.grid(row=0, column=0, sticky="ne", padx=(0, 24), pady=(8, 0))

    def _show_chord(self, chord_name):
        chord_details = self.controller.get_chord_details(chord_name)
        if not chord_details:
            return

        self.current_chord_name = chord_details["name"]
        self.header_title_var.set(chord_details["name"])
        self.chord_label_var.set(chord_details["label"])
        self.chord_info_var.set(self.controller.get_chord_info_text(chord_details))
        self._refresh_mastery_ui(chord_details["mastered"])
        self._draw_chord_diagram(
            strings=chord_details["strings"],
            fingers=chord_details["fingers"],
            fret_count=chord_details["fret_count"],
        )

    def _refresh_mastery_ui(self, is_mastered):
        if is_mastered:
            self.mastery_status_var.set("Status: Mastered")
            if self.mastery_button:
                self.mastery_button.configure(text="Unmark Mastered", fg_color="#666666", hover_color="#555555")
        else:
            self.mastery_status_var.set("Status: Not Mastered")
            if self.mastery_button:
                self.mastery_button.configure(text="Mark as Mastered", fg_color="#2f6f44", hover_color="#245837")

    def _toggle_mastery(self):
        if not self.current_chord_name:
            return

        currently_mastered = self.controller.is_chord_mastered(self.current_chord_name)
        self.controller.set_chord_mastered(self.current_chord_name, mastered=not currently_mastered)
        self._refresh_mastery_ui(not currently_mastered)

    def _toggle_sidebar(self):
        """Open or close the chord selector sidebar."""
        if self.sidebar_panel:
            self.sidebar_panel.animate()

    def close(self):
        self.controller.close()

    def _draw_chord_diagram(self, strings, fingers, fret_count=5):
        if not self.chord_canvas:
            return

        canvas = self.chord_canvas
        canvas.delete("all")

        left = 58
        top = 78
        string_spacing = 40
        fret_spacing = 58
        nut_y = top

        for string_index in range(6):
            x_pos = left + (string_index * string_spacing)
            canvas.create_line(
                x_pos,
                top,
                x_pos,
                top + (fret_count * fret_spacing),
                width=2,
                fill="#333333",
            )

        for fret_index in range(fret_count + 1):
            y_pos = top + (fret_index * fret_spacing)
            line_width = 4 if fret_index == 0 else 2
            canvas.create_line(
                left,
                y_pos,
                left + (5 * string_spacing),
                y_pos,
                width=line_width,
                fill="#333333",
            )

        for string_index, fret in enumerate(strings):
            x_pos = left + (string_index * string_spacing)

            if fret == "X":
                canvas.create_text(
                    x_pos,
                    nut_y - 36,
                    text="X",
                    font=("Arial", 16, "bold"),
                    fill="#444444",
                )
                continue

            if fret == 0:
                canvas.create_text(
                    x_pos,
                    nut_y - 36,
                    text="O",
                    font=("Arial", 16, "bold"),
                    fill="#444444",
                )
                continue

            y_pos = top + ((fret - 1) * fret_spacing) + (fret_spacing / 2)
            canvas.create_oval(
                x_pos - 16,
                y_pos - 16,
                x_pos + 16,
                y_pos + 16,
                fill="#1f9d55",
                outline="#1f9d55",
            )

            finger_number = fingers[string_index]
            if finger_number is not None:
                canvas.create_text(
                    x_pos,
                    y_pos,
                    text=str(finger_number),
                    font=("Arial", 11, "bold"),
                    fill="white",
                )
