from notes import Notebook
from tools import command_check_decorator


@command_check_decorator()
def list_notes(cmd: str, args:[str], notebook: Notebook):
    if cmd != "list":
        return False
    if len(notebook) == 0:
        print("Notebook is empty!")
    notes = notebook.values() if len(args) == 0 else notebook.find_notes(args)
    if len(notes) == 0:
        print("No matching notes found!")
    for note in notes:
        print(note)
    return True
