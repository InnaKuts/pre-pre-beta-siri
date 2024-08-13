from model.addressBook import AddressBook
from notes import Notebook, Note


def add_note(cmd: str, args: [str], notebook: Notebook, addressbook: AddressBook):
    if cmd != "add":
        return False
    title = get_title(args)
    description = input_description()
    tags = input_tags()
    contact = input_contact(addressbook)
    return notebook.add_note(
        Note(
            title=title,
            description=description,
            tags=tags,
            contact=contact
        )
    )


def get_title(args: [str]):
    title = " ".join(args) if args else ""
    while not title:
        title = input("Enter a title: ")
    return title


def input_description():
    lines = []
    line = input("Enter a description [empty line to finish]: ").strip()
    while line:
        lines.append(line)
        line = input().strip()
    return "\n".join(lines)


def input_tags():
    return input("Enter tags [optional]: ").split()


def input_contact(addressbook: AddressBook):
    contact = input("Enter contact [optional]: ").strip()
    while contact and not addressbook.find(contact):
        contact = input(f"Can't find contact `{contact}`. Try another contact: ").strip()
    return contact
