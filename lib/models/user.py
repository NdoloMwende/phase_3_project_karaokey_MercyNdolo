# lib/models/user.py
from lib.database import CURSOR, CONN

class User:
    def __init__(self, name, email, id=None):
        self.id = id
        self.name = name
        self.email = email

    def save(self):
        """Save a new user to the database."""
        CURSOR.execute("INSERT INTO users (name, email) VALUES (?, ?)", (self.name, self.email))
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def get_all(cls):
        """Return all users."""
        rows = CURSOR.execute("SELECT * FROM users").fetchall()
        return [cls(id=row[0], name=row[1], email=row[2]) for row in rows]
