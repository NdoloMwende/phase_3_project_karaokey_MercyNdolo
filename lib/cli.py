from lib.models.room import Room
from lib.models.song import Song
from lib.models.performer import Performer
from lib.models.performance import Performance


def main_menu():
    while True:
        print("\n=====Karaokey Main Menu=====")
        print("1. Manage Rooms")
        print("2. Manage Songs")
        print("3. Manage Performers")
        print("4. Manage Performances")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            room_menu()
        elif choice == "2":
            song_menu()
        elif choice == "3":
            performer_menu()
        elif choice == "4":
            performance_menu()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

def room_menu():
    while True:
        print("\n Room Management")
        print("1. Add Room")
        print("2. View All Rooms")
        print("3. Delete Room")
        print("4. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Room name: ")
            room_type = input("Room type (e.g., Family, Theater): ")
            try:
                capacity = int(input("Capacity: "))
                room = Room(name, room_type, capacity)
                room.save()
                print(f'Room "{name}" added successfully.')
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            rooms = Room.get_all()
            if not rooms:
                print("No rooms found.")
            for room in rooms:
                print(f"{room.id}: {room.name} ({room.room_type}) - Capacity: {room.capacity}")

        elif choice == "3":
            try:
                room_id = int(input("Enter Room ID to delete: "))
                room = Room.find_by_id(room_id)
                if room:
                    room.delete()
                    print("Room deleted.")
                else:
                    print("Room not found.")
            except ValueError:
                print("Invalid ID.")

        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

def song_menu():
    while True:
        print("\n==== Song Management ====")
        print("1. Add Song")
        print("2. View All Songs")
        print("3. Delete Song")
        print("4. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Song title: ")
            artist = input("Artist: ")
            genre = input("Genre: ")
            try:
                song = Song(title, artist, genre)
                song.save()
                print(f'Song "{title}" added successfully.')
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            songs = Song.get_all()
            if not songs:
                print("No songs found.")
            for song in songs:
                print(f"{song.id}: {song.title} by {song.artist} ({song.genre})")

        elif choice == "3":
            try:
                song_id = int(input("Enter Song ID to delete: "))
                song = Song.find_by_id(song_id)
                if song:
                    song.delete()
                    print("Song deleted.")
                else:
                    print("Song not found.")
            except ValueError:
                print("Invalid ID.")

        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

def performer_menu():
    while True:
        print("\nPerformer Management")
        print("1. Add Performer")
        print("2. View All Performers")
        print("3. Delete Performer")
        print("4. Find Performer by Name")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Performer name: ")
            try:
                performer = Performer(name)
                performer.save()
                print(f'Performer "{name}" added successfully.')
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            performers = Performer.get_all()
            if not performers:
                print("No performers found.")
            for performer in performers:
                print(f"{performer.id}: {performer.name}")

        elif choice == "3":
            try:
                performer_id = int(input("Enter Performer ID to delete: "))
                performer = Performer.find_by_id(performer_id)
                if performer:
                    performer.delete()
                    print("Performer deleted.")
                else:
                    print("Performer not found.")
            except ValueError:
                print("Invalid ID.")

        elif choice == "4":
            name = input("Enter performer name: ")
            performer = Performer.find_by_name(name)
            if performer:
                print(f"Found: {performer.id}: {performer.name}")
            else:
                print("Performer not found.")

        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")


def performance_menu():
    while True:
        print("\nPerformance Logging")
        print("1. Log New Performance")
        print("2. View All Performances")
        print("3. Delete Performance")
        print("4. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == "1":
            try:
                performer_id = int(input("Enter Performer ID: "))
                song_id = int(input("Enter Song ID: "))
                room_id = int(input("Enter Room ID: "))
                date = input("Enter date (YYYY-MM-DD): ")
                time = input("Enter time (HH:MM): ")

                performance = Performance(performer_id, song_id, room_id, date, time)
                performance.save()
                print("Performance logged successfully.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            performances = Performance.get_all()
            if not performances:
                print("No performances found.")
            for p in performances:
                print(f"{p['id']}: {p['performer']} sang '{p['song']}' in {p['room']} on {p['date']} at {p['time']}")

        elif choice == "3":
            try:
                performance_id = int(input("Enter Performance ID to delete: "))
                performance = Performance.find_by_id(performance_id)
                if performance:
                    performance.delete()
                    print("Performance deleted.")
                else:
                    print("Performance not found.")
            except ValueError:
                print("Invalid ID.")

        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")
