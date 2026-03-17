import customtkinter as ctk


class SlidePanel(ctk.CTkFrame):
    """Slide panel for lesson buttons with stable snap open/close behavior."""

    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master=parent)

        self.start_pos = start_pos
        self.end_pos = end_pos
        self.width = abs(end_pos - start_pos)

        self.pos = self.start_pos
        self.in_start_pos = True

        self.place(relx=self.start_pos, rely=0.05, relwidth=self.width, relheight=0.9)

    def animate(self):
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backwards()

    def animate_forward(self):
        self.pos = self.end_pos
        self.in_start_pos = False
        self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)

    def animate_backwards(self):
        self.pos = self.start_pos
        self.in_start_pos = True
        self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
