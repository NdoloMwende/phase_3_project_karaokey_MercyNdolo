import sqlite3

CONN = sqlite3.connect('db/database.db')
CURSOR = CONN.cursor()

def create_tables():
    CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS rooms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            room_type TEXT NOT NULL,
            capacity INTEGER NOT NULL
        )
    ''')
    CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS songs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            artist TEXT NOT NULL,
            genre TEXT NOT NULL
        )
    ''')
    CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS performers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS performances (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            performer_id INTEGER NOT NULL,
            song_id INTEGER NOT NULL,
            room_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            FOREIGN KEY (performer_id) REFERENCES performers(id),
            FOREIGN KEY (song_id) REFERENCES songs(id),
            FOREIGN KEY (room_id) REFERENCES rooms(id),
            UNIQUE (room_id, date, time)
        )
    ''')
    CONN.commit()
