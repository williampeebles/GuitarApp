import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from fundamentalsController import FundamentalsController


class SlidePanel(ctk.CTkFrame):
    """Animated sliding panel for lesson buttons."""
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master=parent)
        
        # general attributes
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.width = abs(end_pos - start_pos)
        
        # animation logic
        self.pos = self.start_pos
        self.in_start_pos = True
        
        # layout
        self.place(relx=self.start_pos, rely=0.05, relwidth=self.width, relheight=0.9)
    
    def animate(self):
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backwards()
    
    def animate_forward(self):
        if self.pos == self.end_pos:
            self.in_start_pos = False
            return

        step = 0.008 if self.pos < self.end_pos else -0.008
        next_pos = self.pos + step
        if (step > 0 and next_pos >= self.end_pos) or (step < 0 and next_pos <= self.end_pos):
            next_pos = self.end_pos

        self.pos = next_pos
        self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
        self.after(10, self.animate_forward)
    
    def animate_backwards(self):
        if self.pos == self.start_pos:
            self.in_start_pos = True
            return

        step = -0.008 if self.pos > self.start_pos else 0.008
        next_pos = self.pos + step
        if (step < 0 and next_pos <= self.start_pos) or (step > 0 and next_pos >= self.start_pos):
            next_pos = self.start_pos

        self.pos = next_pos
        self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
        self.after(10, self.animate_backwards)


class FundamentalsTab:
    """
    Fundamentals tab with three buttons stacked vertically in the center.
    Clicking a button switches to a detail page for that topic.
    """

    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg="#f5f5f5")
        self.background_image = None  # Store reference to background image
        self.sidebar_panel = None  # Store reference to sidebar panel
        self.lesson_buttons = {}
        self.quiz_container = None
        self.quiz_status_label = None
        self.start_quiz_button = None
        self.quiz_vars = []
        self.quiz_questions = []
        self.controller = FundamentalsController()
        self._build_layout()

    def _build_layout(self):
        """Build the initial menu view."""
        self._show_menu_view()

    def _show_menu_view(self):
        """Display the main menu with three buttons."""
        self.controller.set_menu_view()
        # Clear frame
        for widget in self.frame.winfo_children():
            widget.destroy()
        
        # Add background image
        IMAGE_PATH = 'guitar_photo.png'
        WIDTH, HEIGHT = 1500, 800
        bg_image = Image.open(IMAGE_PATH).resize((WIDTH, HEIGHT), Image.LANCZOS)
        self.background_image = ImageTk.PhotoImage(bg_image)
        lbl = tk.Label(self.frame, image=self.background_image)
        lbl.image = self.background_image  # Keep a reference
        lbl.place(relx=0.5, rely=0.5, anchor='center')

        # Create three rounded buttons stacked vertically using customtkinter
        button1 = ctk.CTkButton(
            self.frame,
            text="Posture",
            font=("Arial", 18),
            width=1300,
            height=150,
            fg_color="#000000",
            text_color="white",
            hover_color="#333333",
            corner_radius=0,
            border_width=0,
            cursor="hand2",
            bg_color="#1f1913",
            command=lambda: self._show_topic_view("Posture")
        )
        button1.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        button2 = ctk.CTkButton(
            self.frame,
            text="Hand Positioning",
            font=("Arial", 18),
            width=1300,
            height=150,
            fg_color="#000000",
            text_color="white",
            hover_color="#333333",
            corner_radius=0,
            border_width=0,
            cursor="hand2",
            bg_color="#625040",
            command=lambda: self._show_topic_view("Hand Positioning")
        )
        button2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        button3 = ctk.CTkButton(
            self.frame,
            text="Strumming",
            font=("Arial", 18),
            width=1300,
            height=150,
            fg_color="#000000",
            text_color="white",
            hover_color="#333333",
            corner_radius=0,
            border_width=0,
            cursor="hand2",
            bg_color="#222728",
            command=lambda: self._show_topic_view("Strumming")
        )
        button3.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
        
    def _show_topic_view(self, topic_name):
        """Display the detail page for the selected topic with an animated lesson sidebar."""
        self.controller.set_topic(topic_name)
        # Clear frame
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Create main container
        container = ctk.CTkFrame(self.frame, fg_color="transparent")
        container.pack(fill="both", expand=True)

        # Create button container to hold back and lessons buttons
        button_container = ctk.CTkFrame(container, fg_color="transparent")
        button_container.pack(pady=10)
        
        # Add back button
        back_button = ctk.CTkButton(
            button_container,
            text="← Back",
            font=("Arial", 14),
            width=100,
            fg_color="#333333",
            text_color="white",
            hover_color="#555555",
            command=self._show_menu_view
        )
        back_button.pack(side=tk.LEFT, padx=5)
        
        # Add lessons toggle button
        self.toggle_button = ctk.CTkButton(
            button_container,
            text="≡ Lessons",
            font=("Arial", 14),
            width=100,
            fg_color="#333333",
            text_color="white",
            hover_color="#555555",
            command=lambda: self.sidebar_panel.animate() if hasattr(self, 'sidebar_panel') else None
        )
        self.toggle_button.pack(side=tk.LEFT, padx=5)
        
        # Add title
        title_label = ctk.CTkLabel(
            container,
            text=topic_name,
            font=("Arial", 28, "bold"),
            text_color="#000000",
            fg_color="transparent"
        )
        title_label.pack(pady=20)
        
        # Create a frame to hold the content area and sidebar
        content_container = ctk.CTkFrame(container, fg_color="transparent")
        content_container.pack(fill="both", expand=True, padx=20, pady=20)
        content_container.grid_rowconfigure(0, weight=1)
        content_container.grid_columnconfigure(0, weight=1)
        content_container.grid_anchor("center")
        
        # Main content area centered with a fixed width
        main_content = tk.Frame(content_container, bg="white", relief=tk.SUNKEN, bd=1, width=1100, height=700)
        main_content.grid(row=0, column=0)
        main_content.pack_propagate(False)
        
        # Create lesson display area
        lesson_frame = tk.Frame(main_content, bg="white")
        lesson_frame.pack(fill="both", expand=True, padx=12, pady=12)
        
        # Label to show selected lesson
        self.lesson_title_label = tk.Label(
            lesson_frame,
            text="Select a lesson from the sidebar",
            font=("Arial", 18, "bold"),
            bg="white",
            fg="#333333"
        )
        self.lesson_title_label.pack(pady=20)
        
        # Text widget for lesson content
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
            pady=15
        )
        self.lesson_content_text.pack(side=tk.LEFT, fill="both", expand=True)
        
        # Scrollbar for lesson content
        scrollbar = tk.Scrollbar(text_container, command=self.lesson_content_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.lesson_content_text.configure(yscrollcommand=scrollbar.set)
        self.lesson_content_text.configure(state="disabled")

        self.quiz_container = None
        
        # Create animated sidebar panel
        self.sidebar_panel = SlidePanel(content_container, -0.35, 0.0)
        self.sidebar_panel.configure(fg_color="#2b2b2b")
        
        # Update toggle button command now that sidebar exists
        self.toggle_button.configure(command=self.sidebar_panel.animate)
        
        # Add sidebar title
        sidebar_title = ctk.CTkLabel(
            self.sidebar_panel,
            text="Lessons",
            font=("Arial", 16, "bold"),
            text_color="white"
        )
        sidebar_title.pack(pady=10)
        
        # Create scrollable frame for lesson buttons
        scrollable_frame = ctk.CTkScrollableFrame(
            self.sidebar_panel,
            fg_color="#2b2b2b",
            label_text=""
        )
        scrollable_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Add lesson buttons to sidebar
        sample_items = self.controller.get_lessons_for_topic(topic_name)
        self.lesson_buttons = {}
        for lesson_name in sample_items:
            display_text = self.controller.get_lesson_button_text(lesson_name)
            lesson_btn = ctk.CTkButton(
                scrollable_frame,
                text=display_text,
                font=("Arial", 11),
                fg_color="#404040",
                text_color="white",
                hover_color="#505050",
                corner_radius=5,
                command=lambda lesson=lesson_name: self._update_lesson_content(lesson)
            )
            lesson_btn.pack(fill="x", padx=5, pady=5)
            self.lesson_buttons[lesson_name] = lesson_btn
    
    def _update_lesson_content(self, lesson):
        """Update the lesson content display when a sidebar button is clicked."""
        if self.lesson_title_label and self.lesson_content_text:
            self.controller.set_lesson(lesson)
            self.lesson_title_label.configure(text=lesson)
            
            # Get and display lesson content
            lesson_content = self.controller.get_lesson_content(lesson)
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
            font=("Arial", 11)
        )
        self.quiz_status_label.pack(anchor="w")

        self.start_quiz_button = ctk.CTkButton(
            self.quiz_container,
            text="Start 5-Question Quiz",
            font=("Arial", 12),
            fg_color="#333333",
            text_color="white",
            hover_color="#555555",
            command=self._start_quiz
        )
        self.start_quiz_button.pack(anchor="w", pady=(8, 0))

        if not current_lesson:
            self.start_quiz_button.configure(state="disabled")

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
                wraplength=900
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
                    wraplength=900
                )
                choice_btn.pack(anchor="w")

        submit_button = ctk.CTkButton(
            self.quiz_container,
            text="Submit Quiz",
            font=("Arial", 12),
            fg_color="#333333",
            text_color="white",
            hover_color="#555555",
            command=self._submit_quiz
        )
        submit_button.pack(anchor="w", pady=(10, 0))

        self.quiz_status_label = tk.Label(
            self.quiz_container,
            text="",
            bg="white",
            fg="#333333",
            font=("Arial", 11)
        )
        self.quiz_status_label.pack(anchor="w", pady=(6, 0))

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

    def _update_lesson_button_state(self, lesson):
        lesson_btn = self.lesson_buttons.get(lesson)
        if lesson_btn:
            lesson_btn.configure(text=self.controller.get_lesson_button_text(lesson))
    
    def close(self):
        """Close the fundamentals controller and its resources."""
        if self.controller:
            self.controller.close()

