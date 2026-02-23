from tkinter import *
from PIL import Image, ImageTk
from tabController import TabController, DEFAULT_CATEGORIES
from fundamentalsContent import FundamentalsContent
from database import Database
from databaseController import DatabaseController

class GuitarApp:
    def __init__(self):
        self.db = Database()
        self.root = Tk()
        self.root.title("Guitar Learning App")
        self.root.geometry("1500x800")
        
        # App banner with wooden background
        banner_frame = Frame(self.root, relief=RAISED, bd=1, height=100)
        banner_frame.pack(side=TOP, fill=X)
        banner_frame.pack_propagate(False)
        
        # Load and resize wooden background for banner
        try:
            bg_image = Image.open('wooden_bg.jpg')
            banner_height = 100
            bg_image = bg_image.resize((1500, banner_height), Image.LANCZOS)
            banner_bg = ImageTk.PhotoImage(bg_image)
            
            # Use Canvas to overlay text on image
            banner_canvas = Canvas(banner_frame, width=1500, height=100, highlightthickness=0, bd=0)
            banner_canvas.image = banner_bg  # Keep a reference
            banner_canvas.pack(fill=BOTH, expand=True)
            
            # Draw background image on canvas
            banner_canvas.create_image(0, 0, image=banner_bg, anchor=NW)
            
            # Create text on canvas (no background)
            banner_canvas.create_text(750, 50, text="GUITAR APP", font=("Arial", 28, "bold"), fill="#000000")
        except Exception as e:
            # Fallback to black background if image not found
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
        
        # Set up close handler to update database on exit
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
    
    def on_close(self):
        """Update database and close the application."""
        db_controller = DatabaseController()
        db_controller.seed_initial_data(DEFAULT_CATEGORIES, FundamentalsContent.FUNDAMENTALS_LESSONS)
        db_controller.close()
        # Close all database connections
        self.tab_controller.close()
        self.db.close()
        self.root.destroy()
        

if __name__ == "__main__":
    # Initialize database schema
    db = Database()
    db.create_schema()
    db.close()
    
    # Seed initial data
    db_controller = DatabaseController()
    db_controller.seed_initial_data(DEFAULT_CATEGORIES, FundamentalsContent.FUNDAMENTALS_LESSONS)
    db_controller.close()
    
    # Start application
    app = GuitarApp()
    app.root.mainloop()
    
    