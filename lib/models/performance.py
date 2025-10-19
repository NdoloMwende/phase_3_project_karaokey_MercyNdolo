from lib.database import CURSOR, CONN
from lib.logger import log_action
from lib.models.performer import Performer
from lib.models.song import Song
from lib.models.room import Room
import sqlite3

class Performance:
    def __init__(self, performer_id, song_id, room_id, date, time, id=None):
        self.id = id
        self.performer_id = performer_id
        self.song_id = song_id
        self.room_id = room_id
        self.date = date
        self.time = time

    def save(self):
        if not all([self.performer_id, self.song_id, self.room_id, self.date, self.time]):
            raise ValueError("All fields are required.")

        # Validate foreign keys
        if not Performer.find_by_id(self.performer_id):
            raise ValueError("Performer does not exist.")
        if not Song.find_by_id(self.song_id):
            raise ValueError("Song does not exist.")
        if not Room.find_by_id(self.room_id):
            raise ValueError("Room does not exist.")

        try:
            CURSOR.execute(
                '''
                INSERT INTO performances (performer_id, song_id, room_id, date, time)
                VALUES (?, ?, ?, ?, ?)
                ''',
                (self.performer_id, self.song_id, self.room_id, self.date, self.time)
            )
            CONN.commit()
            self.id = CURSOR.lastrowid
            log_action(f'Logged Performance: Performer {self.performer_id}, Song {self.song_id}, Room {self.room_id} on {self.date} at {self.time}')
        except sqlite3.IntegrityError:
            raise ValueError("This room is already booked at that date and time.")

    def delete(self):
        if not self.id:
            raise ValueError("Performance must have an ID to be deleted.")
        CURSOR.execute("DELETE FROM performances WHERE id = ?", (self.id,))
        CONN.commit()
        log_action(f'Deleted Performance ID {self.id}')

    @classmethod
    def get_all(cls):
        rows = CURSOR.execute('''
            SELECT p.id, pf.name, s.title, r.name, p.date, p.time
            FROM performances p
            JOIN performers pf ON p.performer_id = pf.id
            JOIN songs s ON p.song_id = s.id
            JOIN rooms r ON p.room_id = r.id
        ''').fetchall()

        return [{
            "id": row[0],
            "performer": row[1],
            "song": row[2],
            "room": row[3],
            "date": row[4],
            "time": row[5]
        } for row in rows]

    @classmethod
    def find_by_id(cls, performance_id):
        row = CURSOR.execute("SELECT * FROM performances WHERE id = ?", (performance_id,)).fetchone()
        if row:
            return cls(id=row[0], performer_id=row[1], song_id=row[2], room_id=row[3], date=row[4], time=row[5])
        return None
