import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk


class FundamentalsTab:
    """
    Fundamentals tab with three buttons stacked vertically in the center.
    """

    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg="#f5f5f5")
        self._build_layout()

    def _build_layout(self):
        # Add background image
        IMAGE_PATH = 'guitar_photo.png'
        WIDTH, HEIGHT = 1500, 800
        bg_image = Image.open(IMAGE_PATH).resize((WIDTH, HEIGHT), Image.LANCZOS)
        img = ImageTk.PhotoImage(bg_image)
        lbl = tk.Label(self.frame, image=img)
        lbl.img = img  # Keep a reference in case this code put is in a function.
        lbl.place(relx=0.5, rely=0.5, anchor='center')  # Place label in center of parent.

        
        
        # Create three rounded buttons stacked vertically using customtkinter
        # Place each button individually to avoid white space covering background
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
            bg_color="#1f1913"
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
            bg_color="#625040"
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
            bg_color="#222728"
        )
        button3.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
