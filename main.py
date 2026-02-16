from tkinter import *
from tabController import TabController

class GuitarApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("Guitar Learning App")
        self.geometry("1500x800")
        
        # App banner
        banner_frame = Frame(self, bg="#000000", relief=RAISED, bd=1)
        banner_frame.pack(side=TOP, fill=X)
        
        banner_label = Label(
            banner_frame,
            text="GUITAR APP",
            font=("Arial", 28, "bold"),
            bg="#000000",
            fg="white",
            pady=10
        )
        banner_label.pack()
        
        # Create and display the tab controller
        self.tab_controller = TabController(self)
        self.tab_controller.get_notebook().pack(fill="both", expand=True)
        

if __name__ == "__main__":
    app = GuitarApp()
    app.mainloop()
    
    