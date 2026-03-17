import tkinter as tk
import customtkinter as ctk
from maintenanceController import MaintenanceController
from slide_panel import SlidePanel
from woodBackground import WoodBackgroundManager


class MaintenanceTab:
    """Maintenance tab with sectioned lessons in a slide-out panel."""

    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg="#f5f5f5")
        self.controller = MaintenanceController()
        self.sidebar_panel = None
        self.background_manager = WoodBackgroundManager(self.frame)
        self.lesson_buttons = {}
        self.quiz_container = None
        self.quiz_status_label = None
        self.start_quiz_button = None
        self.quiz_vars = []
        self.quiz_questions = []
        self._build_layout()

    def _build_layout(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        self.background_manager.apply()

        content_frame = tk.Frame(self.frame, bg="white", relief=tk.RIDGE, bd=1)
        content_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.82, relheight=0.9)

        header_frame = tk.Frame(content_frame, bg="white")
        header_frame.pack(fill="x", padx=12, pady=(12, 6))

        self.toggle_button = ctk.CTkButton(
            header_frame,
            text="≡ Lessons",
            font=("Arial", 14),
            width=110,
            fg_color="#333333",
            text_color="white",
            hover_color="#555555",
            command=self._toggle_sidebar,
        )
        self.toggle_button.pack(anchor="center")

        content_container = tk.Frame(content_frame, bg="white")
        content_container.pack(fill="both", expand=True, padx=12, pady=(0, 12))
        content_container.grid_rowconfigure(0, weight=1)
        content_container.grid_columnconfigure(0, weight=1)

        self._build_lesson_area(content_container)
        self._build_lesson_sidebar(content_container)

    def _build_lesson_area(self, content_container):
        main_content = tk.Frame(content_container, bg="white", relief=tk.SUNKEN, bd=1)
        main_content.grid(row=0, column=0, sticky="nsew")

        lesson_frame = tk.Frame(main_content, bg="white")
        lesson_frame.pack(fill="both", expand=True, padx=12, pady=12)

        self.lesson_title_label = tk.Label(
            lesson_frame,
            text="Select a lesson from the Lessons button",
            font=("Arial", 18, "bold"),
            bg="white",
            fg="#333333",
        )
        self.lesson_title_label.pack(pady=20)

        text_container = tk.Frame(lesson_frame, bg="white")
        text_container.pack(fill="both", expand=True, padx=20, pady=20)

        self.lesson_content_text = tk.Text(
            text_container,
            bg="white",
            fg="#333333",
            font=("Arial", 12),
            relief=tk.FLAT,
            bd=0,
            wrap=tk.WORD,
            padx=15,
            pady=15,
        )
        self.lesson_content_text.pack(side=tk.LEFT, fill="both", expand=True)

        scrollbar = tk.Scrollbar(text_container, command=self.lesson_content_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.lesson_content_text.configure(yscrollcommand=scrollbar.set, state="disabled")

        self.quiz_container = None

    def _build_lesson_sidebar(self, content_container):
        self.sidebar_panel = SlidePanel(content_container, -0.35, 0.0)
        self.sidebar_panel.configure(fg_color="#2b2b2b")

        sidebar_title = ctk.CTkLabel(
            self.sidebar_panel,
            text="Maintenance Sections",
            font=("Arial", 16, "bold"),
            text_color="white",
        )
        sidebar_title.pack(pady=10)

        scrollable_frame = ctk.CTkScrollableFrame(self.sidebar_panel, fg_color="#2b2b2b", label_text="")
        scrollable_frame.pack(fill="both", expand=True, padx=5, pady=5)

        self.lesson_buttons = {}
        for topic_name in self.controller.get_all_topics():
            topic_label = ctk.CTkLabel(
                scrollable_frame,
                text=topic_name,
                font=("Arial", 13, "bold"),
                text_color="white",
            )
            topic_label.pack(anchor="w", padx=8, pady=(12, 4))

            for lesson_name in self.controller.get_lessons_for_topic(topic_name):
                display_text = self.controller.get_lesson_button_text(lesson_name)
                lesson_btn = ctk.CTkButton(
                    scrollable_frame,
                    text=display_text,
                    font=("Arial", 11),
                    fg_color="#404040",
                    text_color="white",
                    hover_color="#505050",
                    corner_radius=5,
                    command=lambda topic=topic_name, lesson=lesson_name: self._update_lesson_content(topic, lesson),
                )
                lesson_btn.pack(fill="x", padx=5, pady=5)
                self.lesson_buttons[lesson_name] = lesson_btn

    def _toggle_sidebar(self):
        if self.sidebar_panel:
            self.sidebar_panel.animate()

    def _update_lesson_content(self, topic_name, lesson_name):
        self.controller.set_topic(topic_name)
        self.controller.set_lesson(lesson_name)
        self.lesson_title_label.configure(text=lesson_name)

        lesson_content = self.controller.get_lesson_content(lesson_name)
        self.lesson_content_text.configure(state="normal")
        self.lesson_content_text.delete("1.0", tk.END)
        self.lesson_content_text.insert(tk.END, lesson_content)
        self.lesson_content_text.insert(tk.END, "\n\n")

        if self.quiz_container:
            self.quiz_container.destroy()
        self.quiz_container = tk.Frame(self.lesson_content_text, bg="white")
        self.lesson_content_text.window_create(tk.END, window=self.quiz_container)
        self.lesson_content_text.insert(tk.END, "\n")
        self.lesson_content_text.configure(state="disabled")

        self._reset_quiz_ui()

    def _reset_quiz_ui(self):
        if not self.quiz_container:
            return

        for widget in self.quiz_container.winfo_children():
            widget.destroy()

        status_text = ""
        current_lesson = self.controller.get_current_lesson()
        if current_lesson and self.controller.is_lesson_completed(current_lesson):
            status_text = "Status: Completed"

        self.quiz_status_label = tk.Label(
            self.quiz_container,
            text=status_text,
            bg="white",
            fg="#333333",
            font=("Arial", 11),
        )
        self.quiz_status_label.pack(anchor="w")

        self.start_quiz_button = ctk.CTkButton(
            self.quiz_container,
            text="Start 5-Question Quiz",
            font=("Arial", 12),
            fg_color="#333333",
            text_color="white",
            hover_color="#555555",
            command=self._start_quiz,
        )
        self.start_quiz_button.pack(anchor="w", pady=(8, 0))

        if not current_lesson:
            self.start_quiz_button.configure(state="disabled")

        self._bind_quiz_mousewheel(self.quiz_container)

    def _start_quiz(self):
        if not self.controller.get_current_lesson():
            return

        for widget in self.quiz_container.winfo_children():
            widget.destroy()

        self.quiz_questions = self.controller.start_quiz_for_current()
        self.quiz_vars = []

        for index, question in enumerate(self.quiz_questions):
            prompt = tk.Label(
                self.quiz_container,
                text=f"{index + 1}. {question['question']}",
                bg="white",
                fg="#333333",
                font=("Arial", 11, "bold"),
                anchor="w",
                justify="left",
                wraplength=900,
            )
            prompt.pack(anchor="w", pady=(6, 0))

            var = tk.IntVar(value=-1)
            self.quiz_vars.append(var)

            for choice_index, choice in enumerate(question["choices"]):
                choice_btn = tk.Radiobutton(
                    self.quiz_container,
                    text=choice,
                    variable=var,
                    value=choice_index,
                    bg="white",
                    fg="#333333",
                    selectcolor="white",
                    anchor="w",
                    justify="left",
                    wraplength=900,
                )
                choice_btn.pack(anchor="w")

        submit_button = ctk.CTkButton(
            self.quiz_container,
            text="Submit Quiz",
            font=("Arial", 12),
            fg_color="#333333",
            text_color="white",
            hover_color="#555555",
            command=self._submit_quiz,
        )
        submit_button.pack(anchor="w", pady=(10, 0))

        self.quiz_status_label = tk.Label(
            self.quiz_container,
            text="",
            bg="white",
            fg="#333333",
            font=("Arial", 11),
        )
        self.quiz_status_label.pack(anchor="w", pady=(6, 0))

        self._bind_quiz_mousewheel(self.quiz_container)

    def _submit_quiz(self):
        if not self.quiz_questions or not self.quiz_vars:
            return

        selected_indexes = [var.get() for var in self.quiz_vars]
        result = self.controller.submit_quiz_answers(selected_indexes)
        if result["completed_now"]:
            current_lesson = self.controller.get_current_lesson()
            if current_lesson:
                self._update_lesson_button_state(current_lesson)
        if result["message"]:
            self.quiz_status_label.configure(text=result["message"])

    def _update_lesson_button_state(self, lesson_name):
        lesson_btn = self.lesson_buttons.get(lesson_name)
        if lesson_btn:
            lesson_btn.configure(text=self.controller.get_lesson_button_text(lesson_name))

    def _bind_quiz_mousewheel(self, root_widget):
        root_widget.bind("<MouseWheel>", self._on_quiz_mousewheel, add="+")
        for child in root_widget.winfo_children():
            self._bind_quiz_mousewheel(child)

    def _on_quiz_mousewheel(self, event):
        if self.lesson_content_text:
            self.lesson_content_text.yview_scroll(int(-1 * (event.delta / 120)), "units")
        return "break"

    def close(self):
        if self.controller:
            self.controller.close()
