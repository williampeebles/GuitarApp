import tkinter as tk
from tkinter import ttk
from dashboardGUI import DashboardTab
from fundamentalsGUI import FundamentalsTab
from chordsGUI import ChordsTab
from songsGUI import SongsTab
from maintenanceGUI import MaintenanceTab

DEFAULT_CATEGORIES = ("Fundamentals", "Chords", "Songs", "Maintenance")


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
        self.chords_tab = ChordsTab(self.notebook)
        self.notebook.add(self.chords_tab.frame, text="Chords")
        
        # Songs Tab
        self.songs_tab = SongsTab(self.notebook)
        self.notebook.add(self.songs_tab.frame, text="Songs")
        
        # Maintenance Tab
        self.maintenance_tab = MaintenanceTab(self.notebook)
        self.notebook.add(self.maintenance_tab.frame, text="Maintenance")
    
    def get_notebook(self):
        """Returns the notebook widget."""
        return self.notebook
    
    def close(self):
        """Close all tabs and their resources."""
        if self.dashboard_tab:
            self.dashboard_tab.close()
        if self.chords_tab:
            self.chords_tab.close()
        if self.fundamentals_tab:
            self.fundamentals_tab.close()
        if self.maintenance_tab:
            self.maintenance_tab.close()
