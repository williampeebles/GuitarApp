import sqlite3


class Database:
    """Manages database initialization and configuration."""
    
    DATABASE_PATH = 'guitar_app.db'
    
    def __init__(self, database_path=None):
        """Initialize database with optional custom path."""
        self.database_path = database_path or Database.DATABASE_PATH
        self.conn = sqlite3.connect(self.database_path)
        self.cursor = self.conn.cursor()
    
    def create_schema(self):
        """Create the database schema (tables only)."""
        # Create categories table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS categories (
                category_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name_text TEXT NOT NULL,
                number_of_elements INTEGER DEFAULT 0,
                tutorials_completed INTEGER DEFAULT 0,
                tutorials_left INTEGER DEFAULT 0,
                completion_percentage REAL DEFAULT 0.0
            )
        ''')
        
        # Create categoryElements table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS categoryElements (
                element_id INTEGER PRIMARY KEY AUTOINCREMENT,
                category_id INTEGER NOT NULL,
                element_type TEXT NOT NULL,
                completed INTEGER DEFAULT 0,
                experience_points INTEGER DEFAULT 0,
                FOREIGN KEY (category_id) REFERENCES categories (category_id)
            )
        ''')
        
        self.conn.commit()
    
    def close(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()

