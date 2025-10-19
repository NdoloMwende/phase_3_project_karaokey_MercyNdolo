from unicodedata import name
from lib.database import CURSOR, CONN
from lib.logger import log_action

class Performer:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def save(self):
        if not self.name:
            raise ValueError("Name is required.")
        CURSOR.execute(
            "INSERT INTO performers (name) VALUES (?)",
            (self.name,)
        )
        CONN.commit()
        self.id = CURSOR.lastrowid
        log_action(f'Registered Performer "{self.name}"')

    def delete(self):
        if not self.id:
            raise ValueError("Performer must have an ID to be deleted.")
        CURSOR.execute("DELETE FROM performers WHERE id = ?", (self.id,))
        CONN.commit()
        log_action(f'Deleted Performer "{self.name}" (ID: {self.id})')

    @classmethod
    def get_all(cls):
        rows = CURSOR.execute("SELECT * FROM performers").fetchall()
        return [cls(id=row[0], name=row[1]) for row in rows]

    @classmethod
    def find_by_id(cls, performer_id):
        row = CURSOR.execute("SELECT * FROM performers WHERE id = ?", (performer_id,)).fetchone()
        if row:
            return cls(id=row[0], name=row[1])
        return None

    @classmethod
    def find_by_name(cls, name):
        row = CURSOR.execute("SELECT * FROM performers WHERE name = ?", (name,)).fetchone()
        if row:
            return cls(id=row[0], name=row[1])
        return None
