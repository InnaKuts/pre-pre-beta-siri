from ..tools.command_check_decorator import command_check_decorator
from ..tools.pretty_table import pretty_records


@command_check_decorator(
        value_error_message = "Error: The search term should not be empty. Usage: search [name]",
        # key_error = "Error: Contact not found."
)
def search_by_name(args, book):
    search_name = args[0].lower()
    matching_contacts = []

    for contact in book.values():
        if search_name in contact.name.value.lower():
            matching_contacts.append(contact)

    if not matching_contacts:
        return "No contacts found."
    pretty_records(matching_contacts)
    return ""

@command_check_decorator(
        value_error_message = "Error: The search term should not be empty. Usage: search [email]",
        # key_error = "Error: Contact not found."
)
def search_by_email(args, book):
    search_email = args[0].lower()
    matching_contacts = []

    for contact in book.values():
        if contact.email and search_email in contact.email.lower():
            matching_contacts.append(contact)

    if not matching_contacts:
        return "No contacts found."
    pretty_records(matching_contacts)
    return ""

