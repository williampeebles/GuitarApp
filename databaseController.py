import sqlite3
from database import Database


class DatabaseController:
    """Handles all database insert and read operations."""
    
    def __init__(self, database_path=None):
        """Initialize controller with optional custom database path."""
        self.database_path = database_path or Database.DATABASE_PATH
        self.conn = sqlite3.connect(self.database_path)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
    
    # INSERT OPERATIONS
    
    def insert_category(self, name_text, number_of_elements=0, tutorials_completed=0, tutorials_left=0, completion_percentage=0.0):
        """Insert a new category into the database."""
        self.cursor.execute('''
            INSERT INTO categories (name_text, number_of_elements, tutorials_completed, tutorials_left, completion_percentage)
            VALUES (?, ?, ?, ?, ?)
        ''', (name_text, number_of_elements, tutorials_completed, tutorials_left, completion_percentage))
        self.conn.commit()

    def insert_element(self, category_id, element_type, completed=0, experience_points=0):
        """Insert a new element into the database."""
        self.cursor.execute('''
            INSERT INTO categoryElements (category_id, element_type, completed, experience_points)
            VALUES (?, ?, ?, ?)
        ''', (category_id, element_type, completed, experience_points))
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
    
    def seed_initial_data(self, category_names=None, fundamentals_lessons=None):
        """Seed the database with initial categories and lessons."""
        category_names = category_names or ()
        fundamentals_lessons = fundamentals_lessons or ()
        
        # Insert categories if they don't exist
        self.cursor.execute('SELECT name_text FROM categories')
        existing_names = {row[0] for row in self.cursor.fetchall()}
        for category_name in category_names:
            if category_name not in existing_names:
                self.insert_category(category_name)
        
        # Insert fundamentals lessons if they don't exist
        fundamentals_category = self.get_category_by_name("Fundamentals")
        if fundamentals_category:
            fundamentals_id = fundamentals_category["category_id"]
            existing_elements = self.get_elements_by_category(fundamentals_id)
            existing_element_names = {elem["element_type"] for elem in existing_elements}
            
            for lesson_name in fundamentals_lessons:
                if lesson_name not in existing_element_names:
                    self.insert_element(fundamentals_id, lesson_name)
            
            # Update category progress
            self.update_category_progress(fundamentals_id)
    
    def close(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()
