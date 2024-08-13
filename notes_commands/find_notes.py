from notes import Notebook


def find_notes(cmd: str, args: [str], notebook: Notebook):
    if cmd not in ["find", "find-tags", "find-tags-strict"]:
        return False
    if len(notebook) == 0:
        print("Notebook is empty!")
    if len(args) == 0:
        args = input_words()
    if len(args) == 0:
        return "At least one word required to start the search."
    words = {v.strip().lower() for v in args}
    find = cmd == "find"
    match_all = cmd == "find-tags-strict"
    notes = notebook.find_notes_by_title(words, match_all) if find else notebook.find_notes_by_tags(words, match_all)
    notes.sort(key=lambda n: n.uuid)
    if len(notes) == 0:
        print("No matching notes found!")
    for note in notes:
        print(note)
    return True


def input_words():
    return input("Enter at least one word: ").split()
