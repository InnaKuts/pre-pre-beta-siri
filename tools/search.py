from tools.command_check_decorator import command_check_decorator

@command_check_decorator(
        value_error_message = "Error: The search term should not be empty. Usage: search [name]",
        # key_error = "Error: Contact not found."
)
def search_by_name(args, book):
    search_name = args[0].lower()
    matching_contacts = []

    for contact in book.values():
        if search_name in contact.name.value.lower():
            matching_contacts.append(str(contact))

    if not matching_contacts:
        return "No contacts found."
    return matching_contacts
