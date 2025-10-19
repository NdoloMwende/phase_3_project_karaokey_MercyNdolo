# lib/cli.py
from lib.models.user import User
from lib.models.item import Item

def main_menu():
    print("Welcome to the App!")
    print("1. Create a user")
    print("2. List users")
    print("3. Create an item")
    print("4. List items")
    print("5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter name: ")
        email = input("Enter email: ")
        user = User(name, email)
        user.save()
        print("User saved!")
    elif choice == "2":
        users = User.get_all()
        for user in users:
            print(f"{user.id}: {user.name} ({user.email})")
    elif choice == "3":
            name = input("Item name: ")
            price = float(input("Item price: "))
            user_id = int(input("User ID: "))
            item = Item(name, price, user_id)
            item.save()
            print("Item saved!")

    elif choice == "4":
        items = Item.get_all()
        for item in items:
            print(f"{item.id}: {item.name} - ${item.price} (User ID: {item.user_id})")

    elif choice == "5":
        print("Goodbye!")
        return
    else:
        print("Invalid choice!")