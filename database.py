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

        # Remove legacy quiz bank table (questions now live in content files).
        self.cursor.execute('DROP TABLE IF EXISTS testBank')

        # Create songTutorials table for persisted songs tab entries
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS songTutorials (
                song_id INTEGER PRIMARY KEY AUTOINCREMENT,
                title_text TEXT NOT NULL,
                artist_name TEXT NOT NULL DEFAULT '',
                url_text TEXT NOT NULL,
                UNIQUE(title_text, artist_name, url_text)
            )
        ''')

        # Lightweight migration: add artist_name column for older databases.
        self.cursor.execute("PRAGMA table_info(songTutorials)")
        columns = {row[1] for row in self.cursor.fetchall()}
        if "artist_name" not in columns:
            self.cursor.execute(
                "ALTER TABLE songTutorials ADD COLUMN artist_name TEXT NOT NULL DEFAULT ''"
            )
        
        self.conn.commit()
    
    def close(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()

