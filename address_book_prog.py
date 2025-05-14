address_book = {}

def create():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    address_book[name] = phone

def view():
    for name, phone in address_book.items():
        print(f"{name}: {phone}")

def insert():
    create()

def delete():
    name = input("Enter name to delete: ")
    if name in address_book:
        del address_book[name]

def modify():
    name = input("Enter name to modify: ")
    if name in address_book:
        phone = input("Enter new phone: ")
        address_book[name] = phone

while True:
    print("\na) Create b) View c) Insert d) Delete e) Modify f) Exit")
    choice = input("Choose an option: ").lower()
    if choice == 'a':
        create()
    elif choice == 'b':
        view()
    elif choice == 'c':
        insert()
    elif choice == 'd':
        delete()
    elif choice == 'e':
        modify()
    elif choice == 'f':
        break
