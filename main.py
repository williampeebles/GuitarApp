from tkinter import *
from PIL import Image, ImageTk
from tabController import TabController, DEFAULT_CATEGORIES
from fundamentalsContent import FundamentalsContent
from maintenanceContent import MaintenanceContent
from chordsContent import ChordsContent
from database import Database
from databaseController import DatabaseController

class GuitarApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("Guitar Learning App")
        self.root.geometry("1500x800")
        self.banner_source = None
        self.banner_bg = None
        self.banner_canvas = None
        self.banner_image_id = None
        self.banner_text_id = None
        
        # App banner with wooden background
        banner_frame = Frame(self.root, relief=RAISED, bd=1, height=100)
        banner_frame.pack(side=TOP, fill=X)
        banner_frame.pack_propagate(False)
        self.banner_frame = banner_frame
        
        # Load and resize wooden background for banner
        try:
            self.banner_source = Image.open("wooden_bg.jpg")

            # Canvas enables dynamic background redraw as the window size changes.
            self.banner_canvas = Canvas(banner_frame, height=100, highlightthickness=0, bd=0)
            self.banner_canvas.pack(fill=BOTH, expand=True)
            self.banner_image_id = self.banner_canvas.create_image(0, 0, anchor=NW)
            self.banner_text_id = self.banner_canvas.create_text(
                0,
                0,
                text="GUITAR APP",
                font=("Arial", 28, "bold"),
                fill="#000000",
            )

            self.banner_canvas.bind("<Configure>", self._refresh_banner)
            self.root.after(0, self._refresh_banner)
        except Exception:
            # Fallback to black background if image not found
            banner_label = Label(
                banner_frame,
                text="GUITAR APP",
                font=("Arial", 28, "bold"),
                bg="#000000",
                fg="white",
                pady=10
            )
            banner_label.pack(fill=BOTH, expand=True)
        
        # Create and display the tab controller
        self.tab_controller = TabController(self.root)
        self.tab_controller.get_notebook().pack(fill="both", expand=True)
        
        # Set up close handler to update database on exit
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
    
    def on_close(self):
        """Update database and close the application."""
        db_controller = DatabaseController()
        db_controller.seed_initial_data(
            category_names=DEFAULT_CATEGORIES,
            fundamentals_lessons=FundamentalsContent.FUNDAMENTALS_LESSONS,
            maintenance_lessons=MaintenanceContent.MAINTENANCE_LESSONS,
            chord_names=ChordsContent.CHORD_NAMES,
        )
        db_controller.close()
        self.tab_controller.close()
        self.root.destroy()

    def _refresh_banner(self, event=None):
        if not self.banner_canvas or not self.banner_source:
            return

        width = self.banner_canvas.winfo_width()
        height = self.banner_canvas.winfo_height()
        if width <= 1 or height <= 1:
            return

        resized = self.banner_source.resize((width, height), Image.LANCZOS)
        self.banner_bg = ImageTk.PhotoImage(resized)
        self.banner_canvas.itemconfig(self.banner_image_id, image=self.banner_bg)
        self.banner_canvas.coords(self.banner_image_id, 0, 0)
        self.banner_canvas.coords(self.banner_text_id, width // 2, height // 2)
        

if __name__ == "__main__":
    # Initialize database schema
    db = Database()
    db.create_schema()
    db.close()
    
    # Seed initial data
    db_controller = DatabaseController()
    db_controller.seed_initial_data(
        category_names=DEFAULT_CATEGORIES,
        fundamentals_lessons=FundamentalsContent.FUNDAMENTALS_LESSONS,
        maintenance_lessons=MaintenanceContent.MAINTENANCE_LESSONS,
        chord_names=ChordsContent.CHORD_NAMES,
    )
    db_controller.close()
    
    # Start application
    app = GuitarApp()
    app.root.mainloop()
    
    