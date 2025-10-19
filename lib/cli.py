from lib.models.room import Room

def main_menu():
    while True:
        print("\n=====Karaokey Main Menu=====")
        print("1. Manage Rooms")
        print("2. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            room_menu()
        elif choice == "2":
            print("Goodbye!")
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
