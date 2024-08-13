from notes import Notebook


def find_notes(cmd: str, args: [str], notebook: Notebook):
    if cmd not in ["find", "find-strict"]:
        return False
    if len(notebook) == 0:
        print("Notebook is empty!")
    while len(args) == 0:
        args = input_tags()
    match_all = cmd == "find-strict"
    notes = notebook.find_notes(args, match_all)
    notes.sort(key=lambda n: n.uuid)
    if len(notes) == 0:
        print("No matching notes found!")
    for note in notes:
        print(note)
    return True


def input_tags():
    line = input("Enter at least one tag: ")
    tags = line.split()
    return tags
