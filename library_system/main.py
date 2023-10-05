# main.py

# Assuming you've already imported necessary functions from books.py and members.py

import books as bks

import members as mem

def display_menu():
    print("\nLibrary Management System")
    print("----------------------------")
    print("1. Add a new book to the library.")
    print("2. Register a new library member.")
    print("3. Borrow a book.")
    print("4. Return a book.")
    print("5. Display all books.")
    print("6. Display all members.")
    print("7. Exit.")
    print("----------------------------")


def main():
    while True:
        display_menu()

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            title = input("Enter the book's title: ")
            author = input("Enter the book's author: ")
            bks.add_book(title, author)
            pass
        elif choice == "2":
            name = input("What's the name of the member you would like to register? ")
            print(mem.register_member(name))
            pass
        elif choice == "3":
            title = input("What's the title of the book you'd like to borrow? ")
            print(bks.borrow_book(title))
            pass
        elif choice == "4":
            title = input("What's the title of the book you'd like to return? ")
            print(bks.return_book(title))
            pass
        elif choice == "5":
            print(bks.display_books())
            pass
        elif choice == "6":
            print(mem.display_members())
            pass
        elif choice == "7":
            print("Thank you for using the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
if __name__ == "__main__":
    main()

