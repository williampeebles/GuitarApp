import tkinter as tk
from tkinter import ttk
from dashboardGUI import DashboardTab
from fundamnetalsGUI import FundamentalsTab


class TabController:
    """
    Manages a tabbed interface for the Guitar App with 5 main sections.
    
    Creates and manages tabs for: Dashboard, Fundamentals, Chords, Songs, and Maintenance.
    Uses ttk.Notebook to provide a clean tabbed navigation interface.
    
    Attributes:
        parent: The parent widget (usually the main window)
        notebook: The ttk.Notebook widget containing all tabs
        dashboard_tab: Frame for the dashboard content
        fundamentals_tab: Frame for fundamentals content
        chords_tab: Frame for chords content
        songs_tab: Frame for songs content
        maintenance_tab: Frame for maintenance content
    
    Methods:
        create_tabs(): Creates all 5 tabs with placeholder content
        get_notebook(): Returns the notebook widget
    """
    
    def __init__(self, parent):
        """
        Configures the tab style and creates the notebook.
        """
        self.parent = parent
        self._configure_tab_style()
        self.notebook = ttk.Notebook(parent, style="Guitar.TNotebook")
        
        # Create the tabs
        self.dashboard_tab = None
        self.fundamentals_tab = None
        self.chords_tab = None
        self.songs_tab = None
        self.maintenance_tab = None
        
        self.create_tabs()

    def _configure_tab_style(self):
        """Configure tab size and font for the notebook tabs."""
        style = ttk.Style(self.parent)
        style.configure(
            "Guitar.TNotebook.Tab",
            font=("Arial", 14),
            padding=(103, 8)
        )
        style.configure("Guitar.TNotebook")
    
    def create_tabs(self):
        """
        Create all 5 tabs and add them to the notebook.
        Each tab is initialized with a title label.
        """
        # Dashboard Tab
        self.dashboard_tab = DashboardTab(self.notebook)
        self.notebook.add(self.dashboard_tab.frame, text="Dashboard")
        
        # Fundamentals Tab
        self.fundamentals_tab = FundamentalsTab(self.notebook)
        self.notebook.add(self.fundamentals_tab.frame, text="Fundamentals")
        
        # Chords Tab
        self.chords_tab = tk.Frame(self.notebook, bg="#f5f5f5")
        self.notebook.add(self.chords_tab, text="Chords")
        
        chords_label = tk.Label(
            self.chords_tab,
            text="Chords",
            font=("Arial", 24),
            bg="#f5f5f5"
        )
        chords_label.pack(pady=20, padx=20)
        
        # Songs Tab
        self.songs_tab = tk.Frame(self.notebook, bg="#f5f5f5")
        self.notebook.add(self.songs_tab, text="Songs")
        
        songs_label = tk.Label(
            self.songs_tab,
            text="Songs",
            font=("Arial", 24),
            bg="#f5f5f5"
        )
        songs_label.pack(pady=20, padx=20)
        
        # Maintenance Tab
        self.maintenance_tab = tk.Frame(self.notebook, bg="#f5f5f5")
        self.notebook.add(self.maintenance_tab, text="Maintenance")
        
        maintenance_label = tk.Label(
            self.maintenance_tab,
            text="Maintenance",
            font=("Arial", 24),
            bg="#f5f5f5"
        )
        maintenance_label.pack(pady=20, padx=20)
    
    
    
