def search_by_name(args, book):
    search_name = args[0].lower()
    matching_contacts =[]

    for contact in book.values():
        if search_name in contact.name.value.lower():
            matching_contacts.append(str(contact))

    if not matching_contacts:
        return "No contacts found."
    
    return "\n".join(matching_contacts)
