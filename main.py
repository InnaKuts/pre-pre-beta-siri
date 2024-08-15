from prompt_toolkit import PromptSession
from model.addressBook import AddressBook
from tools import parse_input, load_data, save_data
from tools.address_book_functions import add_birthday, add_contact, change_contact, delete_contact, show_all, show_birthday, show_phone, show_upcoming_birthdays, show_contacts_birthdays_within
from tools.completer import CommandCompleter
from tools.search import search_by_name

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
        "contacts-birthdays-within": show_contacts_birthdays_within,
        "search": search_by_name
}

def main():
    book_path = "addressbook.pkl"
    book = load_data(book_path, AddressBook())

    commands = COMMANDS.keys()
    session = PromptSession(completer = CommandCompleter(commands))

    print("Welcome to the Pre-Pre-Beta-Siri bot!")

    while True:
        try:
            user_input = session.prompt('Enter command: ')
            (command, params) = parse_input(user_input)

            if command in commands:
                functionToCall = COMMANDS[command]
                result = functionToCall(params, book)

                if(not isinstance(result, bool) or (result == True)):
                    print(result)
                else:
                    print("Good bye!")
                    break
            else:
                print("Unknown command. Please try again.")

        except KeyboardInterrupt: #Ctrl+C
            break  
        except EOFError: #Ctrl+D
            break

    save_data(book, book_path) 

if __name__ == "__main__":
    main()