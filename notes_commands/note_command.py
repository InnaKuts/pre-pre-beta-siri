from model.addressBook import AddressBook
from notes import Notebook
from .add_note import add_note
from .add_test_data import add_test_data
from tools import command_check_decorator, parse_input
from .delete_note import delete_note
from .list_notes import list_notes
from .find_notes import find_notes
from .update_note import update_note


def note_command(cmd: str, args: [str], notebook: Notebook, addressbook: AddressBook):
    res = main_command(cmd, args, notebook, addressbook)
    if type(res) is bool:
        return res
    else:
        print(res)
        return True


@command_check_decorator()
def main_command(cmd: str, args: [str], notebook: Notebook, addressbook: AddressBook):
    if cmd not in ["note", "notes"]:
        return False
    if len(args) > 0:
        cmd, *args = args
    else:
        cmd, args = parse_input(input("Enter notes command: "))
    if cmd == "help":
        print("Available commands:")
        print(help_string())
        return True
    elif add_test_data(cmd, notebook):
        return True
    elif list_notes(cmd, notebook):
        return True
    elif find_notes(cmd, args, notebook):
        return True
    elif add_note(cmd, args, notebook, addressbook):
        return True
    elif delete_note(cmd, args, notebook):
        return True
    elif update_note(cmd, args, notebook, addressbook):
        return True
    else:
        print("Unknown note command! Available commands are: ")
        print(help_string())
        return True


def help_string():
    return f"""
    `note test-data` - populates the notebook with the new data
    `note list` - list all notes in the notebook
    `note find [words]` - find notes by words in title or tag
    `note find-strict [tags]` - find notes by tags, each note should contain all tags
    `note add [title]` - add new note
    `note delete [words]` - find notes by words and prompt user to delete a note
    `note update [words]` - find notes by words and prompt user to update a note
""".strip("\n")
