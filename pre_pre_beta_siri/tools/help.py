"""
 Файл з функціями, що надають інформацю стосовно формату команд.
"""
def help_command(*args, **kwargs):
    return f"""
    `close` - Closes the application
    `exit` - Closes the application
    `add-contact [name] [phone-number:10]` - adds a contact to the address book 
    `all` - show all contacts
    `change [name] [old phone:10] [new phone:10]` - changes the phone of the contact 
    `delete [name]` - deletes the name from the address book
    `phone [name]` - displays the phone of the contact with the given name
    `add-birthday [name] [dd.mm.yyyy]` - adds a birthday to the contact with the given name
    `show-birthday [name]` - displays the birthday of the contact with the given name
    `birthdays` - show the list of contacts with birthday during following week 
    `contacts-birthdays-within [days]` - show the list of contacts with birthday during following [days] days
    `add-email [name] [email]` - adds an email to the contact with the given name 
    `show-email [name]` - displays the email of the contact with the given name
    `change-email [name] [email:@]` - updates an email of the contact with the given name
    `delete-email [name]` - deletes an email from the contact with the given name
    `add-address [name] [street] [number:3], [zip:5] [city], [country]` - adds an address to the contact with the given name
    `edit-address [name] [street] [number:3], [zip:5] [city], [country]` - changes an address of the contact with the given name
    `show-address [name]` - displays the address of the contact with the given name
    `search-address [phrase]` - search contacts by address
    `remove-address [name]` - removes the address of the contact with the given name
    `search-name [phrase]` - search contacts by name
    `search-email [phrase]` - search contacts by email
    `notes-list` - list all notes in the notebook
    `notes-find [words]` - find notes by words in title or tag
    `notes-find-strict [tags]` - find notes by tags, each note should contain all tags
    `notes-add [title]` - add new note
    `notes-delete [words]` - find notes by words and prompt user to delete a note
    `notes-update [words]` - find notes by words and prompt user to update a note
    `test-data` - populates the addressbook with the new data
    `notes-test-data` - populates the notebook with the new data
""".strip("\n")
