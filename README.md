# Karaokey

Karaokey is a Python command-line application that helps manage the daily activities of a karaoke setup. It allows users to add artists, organize songs, and manage available rooms. Each performance can be logged by linking a performer, a chosen song, and a specific room with a set time. The app uses Object-Oriented Programming principles and ORM to handle data.

---

## Features

- **Room Management**: Add and delete karaoke rooms with type and capacity.
- **Song Management**: Add, view, and delete songs with title, artist, and genre.
- **Artist Management**: Add, view, and delete performer records.
- **Performance Logging**: Record each performance by linking a performer, song, and room at a given date and time.
- **Interactive CLI**: Menu-driven navigation, validated inputs, and looping until user exit.
- **Activity Logging**: All create/delete actions are saved in `lib/logs.txt` with timestamps.
- **Property methods** for model constraints (e.g., `Room.is_family_friendly`)
- **Attribute-based lookup** (e.g., find performer by name)


---

## Technologies Used

- Python 3.x
- SQLite (via `sqlite3`)
- Custom ORM (no external libraries)
- Standard Library only

---

## Project Structure

```
karaokey/
│
├── main.py                     # Entry point: sets up DB and launches CLI
├── README.md                   # Project overview and instructions
├── .gitignore                  # Ignore cache, logs, and database
├── db/
│   └── database.db             # SQLite database file
├── lib/
│   ├── __init__.py             # Package marker
│   ├── cli.py                  # CLI interface and menus
│   ├── database.py             # DB connection and table creation
│   ├── logger.py               # Action logging to logs.txt
│   ├── logs.txt                # Action log file
│   └── models/
│       ├── __init__.py         # Package marker
│       ├── room.py             # Room model
│       ├── song.py             # Song model
│       ├── performer.py        # Performer model
│       └── performance.py      # Performance model
```

---

## Environment Setup

This project uses Pipenv for environment management.

To install and run:

1. Install Pipenv: `pip install pipenv`
2. Navigate to the project folder
3. Run: `pipenv install`
4. Activate: `pipenv shell`
5. Start the app: `python main.py`
6. Use the menu to interact with the system

---

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) for educational purposes. You are free to use, modify, and distribute this code with attribution. Please do not use this project for commercial purposes without permission.

---

## Contributing

This is a school project and not open to external contributions at this time. If you are reviewing this for grading or learning purposes, feel free to explore and adapt the code for your own educational use.

---

## Author

Created by [Mercy Ndolo](https://github.com/NdoloMwende)
