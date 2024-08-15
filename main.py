from prompt_toolkit import PromptSession
from model.addressBook import AddressBook
from model.database import Database
from tools import parse_input, load_data, save_data
from tools.address_book_functions import add_birthday, add_contact, change_contact, delete_contact, show_all, \
    show_birthday, show_phone, show_upcoming_birthdays, show_contacts_birthdays_within
from tools.completer import CommandCompleter
from tools.search import search_by_name

# Import necessary modules and classes
import re
from tools import command_check_decorator, parse_input_validator

# Email validation decorator
def email_validator(func):
    def wrapper(*args, **kwargs):
        email = args[1]  # Assuming email is always the second argument
        if "@" not in email or "." not in email:
            return "Error: Invalid email format."
        return func(*args, **kwargs)
    return wrapper

# New function to add an email to a contact
@email_validator
@command_check_decorator(
        value_error_message="Error: Not enough arguments. Usage: add-email [name] [email]"
        )
def add_email(args, book: AddressBook):
    name, email, *_ = args
    record = book.find(name)
    if record is None:
        raise Exception(f"No '{name}' contact found")
    record.add_email(email)
    return "Email added."

# New function to show an email of a contact
@command_check_decorator(
        index_error_message="Error: Not enough arguments. Usage: show-email [name]",
        key_error_message= "Error: Contact not found"
        )
def show_email(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record is None:
        raise Exception(f"No '{name}' contact found")
    return record.email

# New function to change an email of a contact
@email_validator
@command_check_decorator(
        value_error_message="Error: Not enough arguments. Usage: change-email [name] [new email]"
        )
def change_email(args, book: AddressBook):
    name, new_email, *_ = args
    record = book.find(name)
    if record is None:
        raise Exception(f"No '{name}' contact found")
    record.edit_email(new_email)
    return "Email updated."

# New function to delete an email of a contact
@command_check_decorator(
        value_error_message="Error: Not enough arguments. Usage: delete-email [name]"
        )
def delete_email(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record is None:
        raise Exception(f"No '{name}' contact found")
    record.delete_email()
    return "Email removed."

COMMANDS = {
        "hello": lambda *args: "How can I help you?",
        "close": lambda *args: False,
        "exit": lambda *args: False,

        "add-contact": add_contact,
        "all" : show_all,
        "change": change_contact,
        "delete": delete_contact,
        "phone": show_phone,
        "add-birthday": add_birthday,
        "show-birthday": show_birthday,
        "birthdays": show_upcoming_birthdays,
        "add-email": add_email,  # New command for adding email
        "show-email": show_email,  # New command for showing email
        "change-email": change_email,  # New command for changing email
        "delete-email": delete_email,  # New command for deleting email
        "contacts-birthdays-within": show_contacts_birthdays_within,
        "search": search_by_name,
}

def main():
    book_path = "addressbook.pkl"
    db = load_data(book_path, Database.Default )
   
    commands = COMMANDS.keys()
    session = PromptSession(completer=CommandCompleter(commands))

    print("Welcome to the Pre-Pre-Beta-Siri bot!")

    while True:
        try:
            user_input = session.prompt('Enter command: ')
            (command, params) = parse_input(user_input)

            if command in commands:
                functionToCall = COMMANDS[command]
                result = functionToCall(params, db.address_book)

                if(not isinstance(result, bool) or (result == True)):
                    print(result)
                else:
                    print("Good bye!")
                    break
            else:
                print("Unknown command. Please try again.")

        except KeyboardInterrupt:  # Ctrl+C
            break  
        except EOFError:  # Ctrl+D
            break

    save_data(book_path, db) 

if __name__ == "__main__":
    main()
