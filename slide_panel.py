import customtkinter as ctk


class SlidePanel(ctk.CTkFrame):
    """Animated sliding panel for lesson buttons."""

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
