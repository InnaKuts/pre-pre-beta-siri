"""
Команда для пошуку нотаток.
"""
from ..notes import Notebook
from ..tools.pretty_table import pretty_notes


def find_notes(cmd: str, args: [str], notebook: Notebook):
    if cmd not in ["find", "find-strict"]:
        return False
    if len(notebook) == 0:
        print("Notebook is empty!")
        return True
    strict = cmd == "find-strict"
    notes = find_notes_internal(args, strict, notebook)
    if len(notes) == 0:
        print("No matching notes found!")
    pretty_notes(notes)
    return True


def find_notes_internal(args: [str], strict: bool, notebook: Notebook):
    if len(args) == 0:
        args = input_words()
    if len(args) > 0:
        words = {v.strip().lower() for v in args}
        notes = notebook.find_notes_by_tags(words, strict)
        notes += notebook.find_notes_by_title(words, strict)
        notes += notebook.find_notes_by_description(words, strict)
    else:
        notes = list(notebook.values())
    notes.sort(key=lambda n: n.title.value)
    return notes


def input_words():
    return input("Enter at least one word: ").split()
