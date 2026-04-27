import sqlite3
from rankSystem import RankSystem


class DatabaseController:
    """Handles database schema creation, initialization, and all CRUD operations."""

    DATABASE_PATH = 'guitar_app.db'

    DEFAULT_XP_BY_CATEGORY = {
        "Fundamentals": RankSystem.LESSON_XP,
        "Maintenance": RankSystem.LESSON_XP,
        "Chords": RankSystem.CHORD_XP,
    }
    
    def __init__(self, database_path=None):
        """Initialize controller with optional custom database path."""
        self.database_path = database_path or DatabaseController.DATABASE_PATH
        self.conn = sqlite3.connect(self.database_path)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
    
    def create_schema(self):
        """Create the database schema (tables and migrations)."""
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
    
    # INSERT OPERATIONS
    
    def insert_category(self, name_text, number_of_elements=0, tutorials_completed=0, tutorials_left=0, completion_percentage=0.0):
        """Insert a new category into the database."""
        self.cursor.execute('''
            INSERT INTO categories (name_text, number_of_elements, tutorials_completed, tutorials_left, completion_percentage)
            VALUES (?, ?, ?, ?, ?)
        ''', (name_text, number_of_elements, tutorials_completed, tutorials_left, completion_percentage))
        self.conn.commit()

    def _get_default_element_xp(self, category_id):
        """Return default XP for an element based on its category."""
        self.cursor.execute(
            'SELECT name_text FROM categories WHERE category_id = ?',
            (category_id,)
        )
        row = self.cursor.fetchone()
        if not row:
            return 0
        category_name = row[0]
        return self.DEFAULT_XP_BY_CATEGORY.get(category_name, 0)

    def insert_element(self, category_id, element_type, completed=0, experience_points=None):
        """Insert a new element into the database."""
        if experience_points is None:
            experience_points = self._get_default_element_xp(category_id)

        self.cursor.execute('''
            INSERT INTO categoryElements (category_id, element_type, completed, experience_points)
            VALUES (?, ?, ?, ?)
        ''', (category_id, element_type, completed, experience_points))
        self.conn.commit()

    def insert_song_tutorial(self, title_text, url_text, artist_name=""):
        """Insert a song tutorial entry if it does not already exist."""
        self.cursor.execute(
            '''
            INSERT OR IGNORE INTO songTutorials (title_text, artist_name, url_text)
            VALUES (?, ?, ?)
            ''',
            (title_text, artist_name, url_text),
        )
        self.conn.commit()

    def get_song_tutorials(self):
        """Retrieve all persisted song tutorial entries."""
        self.cursor.execute(
            '''
            SELECT title_text, artist_name, url_text
            FROM songTutorials
            ORDER BY song_id
            '''
        )
        rows = self.cursor.fetchall()
        return [
            {
                "title_text": row["title_text"],
                "artist_name": row["artist_name"],
                "url_text": row["url_text"],
            }
            for row in rows
        ]

    def delete_song_tutorial(self, title_text, url_text):
        """Delete a specific persisted song tutorial entry."""
        self.cursor.execute(
            '''
            DELETE FROM songTutorials
            WHERE title_text = ? AND url_text = ?
            ''',
            (title_text, url_text),
        )
        self.conn.commit()

    # READ OPERATIONS
    
    def get_all_categories(self):
        """Retrieve all categories from the database."""
        self.cursor.execute('SELECT * FROM categories')
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]

    def get_category_by_id(self, category_id):
        """Retrieve a specific category by ID."""
        self.cursor.execute('SELECT * FROM categories WHERE category_id = ?', (category_id,))
        row = self.cursor.fetchone()
        return dict(row) if row else None

    def get_category_by_name(self, name_text):
        """Retrieve a specific category by name."""
        self.cursor.execute('SELECT * FROM categories WHERE name_text = ?', (name_text,))
        row = self.cursor.fetchone()
        return dict(row) if row else None

    def get_elements_by_category(self, category_id):
        """Retrieve all elements for a specific category."""
        self.cursor.execute('SELECT * FROM categoryElements WHERE category_id = ?', (category_id,))
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]

    def get_element_by_id(self, element_id):
        """Retrieve a specific element by ID."""
        self.cursor.execute('SELECT * FROM categoryElements WHERE element_id = ?', (element_id,))
        row = self.cursor.fetchone()
        return dict(row) if row else None

    def mark_element_completed(self, category_id, element_type, completed=1):
        """Mark a lesson element as completed and refresh category progress."""
        self.cursor.execute('''
            UPDATE categoryElements
            SET completed = ?
            WHERE category_id = ? AND element_type = ?
        ''', (completed, category_id, element_type))
        self.conn.commit()
        self.update_category_progress(category_id)

    def update_category_progress(self, category_id):
        """Recalculate counts and completion percentage for a category."""
        self.cursor.execute(
            'SELECT COUNT(*) FROM categoryElements WHERE category_id = ?',
            (category_id,)
        )
        total = self.cursor.fetchone()[0]
        self.cursor.execute(
            'SELECT COUNT(*) FROM categoryElements WHERE category_id = ? AND completed = 1',
            (category_id,)
        )
        completed_count = self.cursor.fetchone()[0]
        tutorials_left = max(total - completed_count, 0)
        completion_percentage = round((completed_count * 100.0) / total, 2) if total else 0.0
        self.cursor.execute('''
            UPDATE categories
            SET number_of_elements = ?,
                tutorials_completed = ?,
                tutorials_left = ?,
                completion_percentage = ?
            WHERE category_id = ?
        ''', (total, completed_count, tutorials_left, completion_percentage, category_id))
        self.conn.commit()
    
    def seed_initial_data(
        self,
        category_names=None,
        fundamentals_lessons=None,
        maintenance_lessons=None,
        chord_names=None,
    ):
        """Seed the database with all initial data on first launch."""
        self._remove_legacy_songs_category()
        self._seed_categories(category_names or ())
        self._seed_fundamentals_lessons(fundamentals_lessons or ())
        self._seed_maintenance_lessons(maintenance_lessons or ())
        self._seed_chords(chord_names or ())

    def _remove_legacy_songs_category(self):
        """Remove the old Songs category row and any linked elements."""
        songs_category = self.get_category_by_name("Songs")
        if not songs_category:
            return

        songs_id = songs_category["category_id"]
        self.cursor.execute(
            'DELETE FROM categoryElements WHERE category_id = ?',
            (songs_id,),
        )
        self.cursor.execute(
            'DELETE FROM categories WHERE category_id = ?',
            (songs_id,),
        )
        self.conn.commit()

    def _seed_categories(self, category_names):
        """Insert any category that does not already exist in the database."""
        self.cursor.execute("SELECT name_text FROM categories")
        existing_names = {row[0] for row in self.cursor.fetchall()}
        for category_name in category_names:
            if category_name not in existing_names:
                self.insert_category(category_name)

    def _seed_fundamentals_lessons(self, fundamentals_lessons):
        """Insert any Fundamentals lesson element that does not already exist."""
        fundamentals_category = self.get_category_by_name("Fundamentals")
        if not fundamentals_category:
            return
        fundamentals_id = fundamentals_category["category_id"]
        existing_elements = self.get_elements_by_category(fundamentals_id)
        self._backfill_category_element_xp(fundamentals_id, existing_elements)
        existing_names = {elem["element_type"] for elem in existing_elements}
        for lesson_name in fundamentals_lessons:
            if lesson_name not in existing_names:
                self.insert_element(fundamentals_id, lesson_name)
        self.update_category_progress(fundamentals_id)

    def _seed_maintenance_lessons(self, maintenance_lessons):
        """Insert any Maintenance lesson element that does not already exist."""
        maintenance_category = self.get_category_by_name("Maintenance")
        if not maintenance_category:
            return
        maintenance_id = maintenance_category["category_id"]
        existing_elements = self.get_elements_by_category(maintenance_id)
        self._backfill_category_element_xp(maintenance_id, existing_elements)
        existing_names = {elem["element_type"] for elem in existing_elements}
        for lesson_name in maintenance_lessons:
            if lesson_name not in existing_names:
                self.insert_element(maintenance_id, lesson_name)
        self.update_category_progress(maintenance_id)

    def _seed_chords(self, chord_names):
        """Insert any Chords element that does not already exist."""
        chords_category = self.get_category_by_name("Chords")
        if not chords_category:
            return
        chords_id = chords_category["category_id"]
        existing_elements = self.get_elements_by_category(chords_id)
        self._backfill_category_element_xp(chords_id, existing_elements)
        existing_names = {elem["element_type"] for elem in existing_elements}
        for chord_name in chord_names:
            if chord_name not in existing_names:
                self.insert_element(chords_id, chord_name)
        self.update_category_progress(chords_id)

    def _backfill_category_element_xp(self, category_id, elements):
        """Ensure older elements have XP values set based on category defaults."""
        default_xp = self._get_default_element_xp(category_id)
        if default_xp <= 0:
            return

        missing_xp_ids = [
            element["element_id"]
            for element in elements
            if int(element.get("experience_points") or 0) <= 0
        ]
        if not missing_xp_ids:
            return

        self.cursor.executemany(
            'UPDATE categoryElements SET experience_points = ? WHERE element_id = ?',
            [(default_xp, element_id) for element_id in missing_xp_ids],
        )
        self.conn.commit()

    def close(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()
