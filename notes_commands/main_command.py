from model.addressBook import AddressBook
from notes import Notebook
from .add_note import add_note
from .add_test_data import add_test_data
from tools import command_check_decorator, parse_input
from .delete_note import delete_note
from .list_notes import list_notes
from .find_notes import find_notes
from .update_note import update_note


def make_command(subcommand: str = None):
    @command_check_decorator()
    def command(args: [str], addressbook: AddressBook, notebook: Notebook):
        main_command(subcommand, args, notebook, addressbook)
        return ""

    return command


def main_command(cmd: str, args: [str], notebook: Notebook, addressbook: AddressBook):
    if not cmd:
        cmd, args = parse_input(input("Enter notes command: "))
    if cmd == "help":
        print("Available commands:")
        print(help_string())
    elif add_test_data(cmd, notebook):
        return
    elif list_notes(cmd, notebook):
        return
    elif find_notes(cmd, args, notebook):
        return
    elif add_note(cmd, args, notebook, addressbook):
        return
    elif delete_note(cmd, args, notebook):
        return
    elif update_note(cmd, args, notebook, addressbook):
        return
    else:
        print("Unknown note command! Available commands are: ")
        print(help_string())
        return


def help_string():
    return f"""
    `notes-test-data` - populates the notebook with the new data
    `notes-list` - list all notes in the notebook
    `notes-find [words]` - find notes by words in title or tag
    `notes-find-strict [tags]` - find notes by tags, each note should contain all tags
    `notes-add [title]` - add new note
    `notes-delete [words]` - find notes by words and prompt user to delete a note
    `notes-update [words]` - find notes by words and prompt user to update a note
""".strip("\n")
