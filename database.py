import sqlite3


class Database:
    """Manages database initialization and configuration."""
    
    DATABASE_PATH = 'guitar_app.db'
    
    @staticmethod
    def initialize_database():
        """Create the SQLite database with categoryElements and categories tables.
        
        This should only be called once during initial setup, not every time the app runs.
        """
        conn = sqlite3.connect(Database.DATABASE_PATH)
        cursor = conn.cursor()
        
        # Create categories table
        cursor.execute('''
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
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS categoryElements (
                element_id INTEGER PRIMARY KEY AUTOINCREMENT,
                category_id INTEGER NOT NULL,
                element_type TEXT NOT NULL,
                completed INTEGER DEFAULT 0,
                experience_points INTEGER DEFAULT 0,
                FOREIGN KEY (category_id) REFERENCES categories (category_id)
            )
        ''')
        
        conn.commit()
        conn.close()

