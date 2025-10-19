from lib.database import CURSOR, CONN
from lib.logger import log_action

class Room:
    def __init__(self, name, room_type, capacity, id=None):
        self.id = id
        self.name = name
        self.room_type = room_type
        self.capacity = capacity

    def save(self):
        if not self.name or not self.room_type or not isinstance(self.capacity, int):
            raise ValueError("All fields are required and capacity must be an integer.")
        CURSOR.execute(
            "INSERT INTO rooms (name, room_type, capacity) VALUES (?, ?, ?)",
            (self.name, self.room_type, self.capacity)
        )
        CONN.commit()
        self.id = CURSOR.lastrowid
        log_action(f'Created Room "{self.name}" ({self.room_type}) with capacity {self.capacity}')

    def delete(self):
        if not self.id:
            raise ValueError("Room must have an ID to be deleted.")
        CURSOR.execute("DELETE FROM rooms WHERE id = ?", (self.id,))
        CONN.commit()
        log_action(f'Deleted Room "{self.name}" (ID: {self.id})')

    @classmethod
    def get_all(cls):
        rows = CURSOR.execute("SELECT * FROM rooms").fetchall()
        return [cls(id=row[0], name=row[1], room_type=row[2], capacity=row[3]) for row in rows]

    @classmethod
    def find_by_id(cls, room_id):
        row = CURSOR.execute("SELECT * FROM rooms WHERE id = ?", (room_id,)).fetchone()
        if row:
            return cls(id=row[0], name=row[1], room_type=row[2], capacity=row[3])
        return None

    @property
    def is_family_friendly(self):
        return self.room_type.lower() == 'family'

# if room.is_family_friendly:
#     print("This room is suitable for families.")

    def __str__(self):
        return f'Room ID: {self.id}, Name: {self.name}, Type: {self.room_type}, Capacity: {self.capacity}'