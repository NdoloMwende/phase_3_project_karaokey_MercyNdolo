from lib.database import CURSOR, CONN

class Item:
    def __init__(self, name, price, user_id, id=None):
        self.id = id
        self.name = name
        self.price = price
        self.user_id = user_id

    def save(self):
        CURSOR.execute(
            "INSERT INTO items (name, price, user_id) VALUES (?, ?, ?)",
            (self.name, self.price, self.user_id)
        )
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def get_all(cls):
        rows = CURSOR.execute("SELECT * FROM items").fetchall()
        return [cls(id=row[0], name=row[1], price=row[2], user_id=row[3]) for row in rows]
