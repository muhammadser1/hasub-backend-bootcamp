import sys

from operations.record_crud import *
from operations.record_printer import *
from utils.get_integer_input import get_integer_input


def show_menu():
    """Display the menu options."""
    print("Menu Options:")
    print("1. Add record")
    print("2. Delete record")
    print("3. Search based on name")
    print("4. Update name")
    print("5. Update amount")
    print("6. Print Total Amount")
    print("7. Print sorted collection")
    print("8. Exit")


def cli_interface():
    """Main function to run the user interface."""
    while True:
        show_menu()
        choice = get_integer_input("Enter your choice:", 1, 8)
        if choice == 1:
            name = input("Enter the name ")
            choice = get_integer_input("Enter your amount:", 1)
            add_record(name, choice)

        elif choice == 2:
            name = input("Enter the name ")
            choice = get_integer_input("Enter your amount:", 1)
            delete_record(name, choice)

        elif choice == 3:
            name = input("Enter the name to search for: ")
            search(name, True)

        elif choice == 4:
            old_name = input("Enter the old_name ")
            new_name = input("Enter the new_name ")
            update_record_name(old_name, new_name)

        elif choice == 5:
            name = input("Enter the name of the record to add: ")
            choice = get_integer_input("Enter your amount:")
            update_record_amount(name, choice)

        elif choice == 6:
            PrintTotalAmount()

        elif choice == 7:
            PrintAll()

        elif choice == 8:
            print("Exiting the program.")
            sys.exit()
