from model.addressBook import AddressBook
from notes import Notebook, Note


def add_note(cmd: str, args: [str], notebook: Notebook, addressbook: AddressBook):
    if cmd != "add":
        return False
    title = get_title(args)
    description = input_description()
    tags = input_tags()
    contact = input_contact(addressbook)
    res = notebook.add_note(
        Note(
            title=title,
            description=description,
            tags=tags,
            contact=contact
        )
    )
    print("Note added!" if res else "Failed to add a note")
    return True


def get_title(args: [str], default: str = ""):
    title = " ".join(args) if args else ""
    default_format = f" [{default}]" if default else ""
    while not title:
        title = input(f"Enter a title{default_format}: ") or default
    return title


def input_description(default: str = ""):
    lines = []
    default_format = f"[{repr(default)}]" if default else "[empty line to finish]"
    line = input(f"Enter a description {default_format}: ").strip()
    while line:
        lines.append(line)
        line = input().strip()
    return "\n".join(lines) or default


def input_tags(default: [str] = None):
    default_format = f"[{';'.join(default)}]" if default else "[optional]"
    return input(f"Enter tags {default_format}: ").split() or default


def input_contact(addressbook: AddressBook, default: str = ""):
    default_format = f"[{default}]" if default else "[optional]"
    contact = input(f"Enter contact {default_format}: ").strip()
    while contact and not addressbook.find(contact):
        contact = input(f"Can't find contact `{contact}`. Try another contact: ").strip()
    return contact or default
