from notes import Notebook
from .find_notes import find_notes_internal


def delete_note(cmd: str, args: [str], notebook: Notebook):
    if cmd not in ["delete"]:
        return False
    if len(notebook) == 0:
        print("Notebook is empty!")
        return True
    notes = find_notes_internal(args, False, notebook)
    if len(notes) == 0:
        print("No matching notes found!")
        return True
    for (index, note) in enumerate(notes):
        print(f"[{index + 1}]: {note}")
    index = input_index()
    if not index or index < 1 or index > len(notes):
        print("Invalid note index")
        return True
    index -= 1
    res = notebook.delete_note(notes[index].uuid)
    print("Note deleted!" if res else "Failed to delete a note!")
    return True


def input_index():
    line = input("Enter number of note to delete: ").strip()
    try:
        return int(line)
    except Exception:
        return None
