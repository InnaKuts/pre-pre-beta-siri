from notes import Notebook
from tools import command_check_decorator
from tools.pretty_table import pretty_notes


def list_notes(cmd: str, notebook: Notebook):
    if cmd not in ["list"]:
        return False
    if len(notebook) == 0:
        print("Notebook is empty!")
    notes = list(notebook.values())
    notes.sort(key=lambda n: n.title.value)
    if len(notes) == 0:
        print("No matching notes found!")
    pretty_notes(notes)
    return True
