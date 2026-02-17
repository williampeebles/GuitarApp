import sqlite3
from database import Database


class DatabaseController:
    """Handles all database insert and read operations."""
    
    # INSERT OPERATIONS
    
    def insert_category(self, name_text, number_of_elements=0, tutorials_completed=0, tutorials_left=0, completion_percentage=0.0):
        """Insert a new category into the database."""
        conn = sqlite3.connect(Database.DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO categories (name_text, number_of_elements, tutorials_completed, tutorials_left, completion_percentage)
            VALUES (?, ?, ?, ?, ?)
        ''', (name_text, number_of_elements, tutorials_completed, tutorials_left, completion_percentage))
        conn.commit()
        conn.close()

    def insert_element(self, category_id, element_type, completed=0, experience_points=0):
        """Insert a new element into the database."""
        conn = sqlite3.connect(Database.DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO categoryElements (category_id, element_type, completed, experience_points)
            VALUES (?, ?, ?, ?)
        ''', (category_id, element_type, completed, experience_points))
        conn.commit()
        conn.close()

    # READ OPERATIONS
    
    def get_all_categories(self):
        """Retrieve all categories from the database."""
        conn = sqlite3.connect(Database.DATABASE_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM categories')
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    def get_category_by_id(self, category_id):
        """Retrieve a specific category by ID."""
        conn = sqlite3.connect(Database.DATABASE_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM categories WHERE category_id = ?', (category_id,))
        row = cursor.fetchone()
        conn.close()
        return dict(row) if row else None

    def get_elements_by_category(self, category_id):
        """Retrieve all elements for a specific category."""
        conn = sqlite3.connect(Database.DATABASE_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM categoryElements WHERE category_id = ?', (category_id,))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    def get_element_by_id(self, element_id):
        """Retrieve a specific element by ID."""
        conn = sqlite3.connect(Database.DATABASE_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM categoryElements WHERE element_id = ?', (element_id,))
        row = cursor.fetchone()
        conn.close()
        return dict(row) if row else None
