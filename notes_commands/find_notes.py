from notes import Notebook


def find_notes(cmd: str, args: [str], notebook: Notebook):
    if cmd not in ["find", "find-tags", "find-tags-strict"]:
        return False
    if len(notebook) == 0:
        print("Notebook is empty!")
        return True
    by_title = cmd == "find"
    strict = cmd == "find-tags-strict"
    notes = find_notes_internal(args, by_title, strict, notebook)
    if len(notes) == 0:
        print("No matching notes found!")
    for note in notes:
        print(note)
    return True


def find_notes_internal(args: [str], by_title: bool, strict: bool, notebook: Notebook):
    if len(args) == 0:
        args = input_words()
    if len(args) == 0:
        raise Exception("At least one word required to start the search.")
    words = {v.strip().lower() for v in args}
    notes = notebook.find_notes_by_title(words, strict) if by_title else notebook.find_notes_by_tags(words, strict)
    notes.sort(key=lambda n: n.uuid)
    return notes


def input_words():
    return input("Enter at least one word: ").split()
