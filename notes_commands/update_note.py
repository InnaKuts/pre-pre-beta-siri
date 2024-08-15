from model.addressBook import AddressBook
from notes import Notebook, Note
from .add_note import get_title, input_description, input_tags, input_contact
from .find_notes import find_notes_internal


def update_note(cmd: str, args: [str], notebook: Notebook, addressbook: AddressBook):
    if cmd not in ["update"]:
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
    note = notes[index]
    title = get_title([], note.title.value)
    description = input_description(note.description.value)
    tags = input_tags(note.tags.value)
    contact = input_contact(addressbook, note.contact.value if note.contact else None)
    res = notebook.update_note(
        Note(
            title=title,
            description=description,
            tags=tags,
            contact=contact,
            uuid=note.uuid,
        )
    )
    print("Note updated!" if res else "Failed to update a note")
    return True


def input_index():
    line = input("Enter number of note to update: ").strip()
    try:
        return int(line)
    except Exception:
        return None
