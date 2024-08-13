from model.addressBook import AddressBook
from notes import Notebook
from tools import command_check_decorator


@command_check_decorator
def note_command(cmd: str, args: [str], notebook: Notebook, addressbook: AddressBook):
    if cmd not in ["note", "notes"]:
        return False
    return False
