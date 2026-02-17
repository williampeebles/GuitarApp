from tkinter import *
from tabController import TabController

class GuitarApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("Guitar Learning App")
        self.root.geometry("1500x800")
        
        # App banner
        banner_frame = Frame(self.root, bg="#000000", relief=RAISED, bd=1)
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
        self.tab_controller = TabController(self.root)
        self.tab_controller.get_notebook().pack(fill="both", expand=True)
        

if __name__ == "__main__":
    app = GuitarApp()
    app.root.mainloop()
    
    