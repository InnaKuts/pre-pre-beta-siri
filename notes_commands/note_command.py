from model.addressBook import AddressBook
from notes import Notebook
from .add_test_data import add_test_data
from tools import command_check_decorator, parse_input
from .list_notes import list_notes


@command_check_decorator()
def note_command(cmd: str, args: [str], notebook: Notebook, addressbook: AddressBook):
    if cmd not in ["note", "notes"]:
        return False
    if len(args) > 0:
        cmd, *args = args
    else:
        cmd, args = parse_input(input("Enter notes command: "))
    if add_test_data(cmd, notebook):
        return True
    elif list_notes(cmd, args, notebook):
        return True
    else:
        print("Unknown note command!")
        return False
