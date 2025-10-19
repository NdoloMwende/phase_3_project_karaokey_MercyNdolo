from lib.database import CURSOR, CONN
from lib.logger import log_action

class Song:
    def __init__(self, title, artist, genre, id=None):
        self.id = id
        self.title = title
        self.artist = artist
        self.genre = genre

    def save(self):
        if not self.title or not self.artist or not self.genre:
            raise ValueError("All fields are required.")
        CURSOR.execute(
            "INSERT INTO songs (title, artist, genre) VALUES (?, ?, ?)",
            (self.title, self.artist, self.genre)
        )
        CONN.commit()
        self.id = CURSOR.lastrowid
        log_action(f'Added Song "{self.title}" by {self.artist} ({self.genre})')

    def delete(self):
        if not self.id:
            raise ValueError("Song must have an ID to be deleted.")
        CURSOR.execute("DELETE FROM songs WHERE id = ?", (self.id,))
        CONN.commit()
        log_action(f'Deleted Song "{self.title}" (ID: {self.id})')

    @classmethod
    def get_all(cls):
        rows = CURSOR.execute("SELECT * FROM songs").fetchall()
        return [cls(id=row[0], title=row[1], artist=row[2], genre=row[3]) for row in rows]

    @classmethod
    def find_by_id(cls, song_id):
        row = CURSOR.execute("SELECT * FROM songs WHERE id = ?", (song_id,)).fetchone()
        if row:
            return cls(id=row[0], title=row[1], artist=row[2], genre=row[3])
        return None
