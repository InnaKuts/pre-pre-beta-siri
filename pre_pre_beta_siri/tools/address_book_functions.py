
from ..model.addressBook import AddressBook
from ..model.record import Record
from ..tools import command_check_decorator
from ..tools.pretty_table import pretty_records


@command_check_decorator(
        value_error_message="Error: Not enough arguments. Usage: add [name] [phone number]"
        ) 
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    else:
        message = "Contact with this name already exists. Please try again with a different name."
        return message
    if phone:
        record.add_phone(phone)
    return message


@command_check_decorator(
        value_error_message="Error: Not enough arguments. Usage: change [name] [old phone] [new phone number]"
        ) 
def change_contact(args, book:AddressBook):
    name, old_phone, new_phone = args
    if name in book:
        r = book[name]
        r.edit_phone(old_phone, new_phone)
        return "Contact updated."
    else:
        raise Exception("Error: Contact not found.")


@command_check_decorator(
        index_error_message="Error: Not enough arguments. Usage: delete [name]",
        key_error_message= "Error: Contact not found"
        ) 
def delete_contact(args, book:AddressBook):
    name = args[0]
    book.pop(name)
    return "Contact removed."


@command_check_decorator(
        index_error_message="Error: Not enough arguments. Usage: phone [name]",
        key_error_message= "Error: Contact not found"
        )
def show_phone(args, book:AddressBook):
    name = args[0]
    contact_strings = [p.value for p in book[name].phones]
    result = ", ".join(contact_strings)
    return result


def show_all(args, book:AddressBook):
    if len(book) == 0:
        return "No contacts found."
    pretty_records(book.data.values())
    return ""


@command_check_decorator(
        value_error_message="Error: Not enough arguments. Usage: add-birthday [name] [birthday (DD.MM.YYYY)]"
        ) 
def add_birthday(args, book: AddressBook):
    name, birthday, *_ = args
    record = book.find(name)
    if record is None:
        raise Exception(f"No '{name}' contact found")
    record.add_birthday(birthday)
    return "Contact updated"


@command_check_decorator(
        index_error_message="Not valid contact names"
        )
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record is None:
        raise Exception(f"No '{name}' contact found")
    return record.birthday.value.strftime("%d.%m.%Y") if record.birthday != None else "N/A"


def show_upcoming_birthdays(args, book: AddressBook):
    items = book.get_upcoming_birthdays()
    birthday_strings = [f"{x['name']} - {x['congratulation_date']}" for x in items]
    result = "\n".join(birthday_strings)
    return result


@command_check_decorator(value_error_message="Error: Not enough arguments. Usage: add-address [name] [address]")
def add_address(args, book: AddressBook):
    name = args[0]
    address = ' '.join(args[1:])
    record = book.find(name)
    if record is None:
        raise Exception(f"No contact found with name: {name}")
    record.add_address(address)
    return "Address added."


@command_check_decorator(value_error_message="Error: Not enough arguments. Usage: edit-address [name] [new address]")
def edit_address(args, book: AddressBook):
    name = args[0]
    address = ' '.join(args[1:])
    record = book.find(name)
    if record is None:
        raise Exception(f"No contact found with name: {name}")
    record.edit_address(address)
    return "Address updated."


@command_check_decorator(index_error_message="Error: Not enough arguments. Usage: show-address [name]")
def show_address(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record is None or not record.address:
        return "No address found for this contact."
    return str(record.address)


@command_check_decorator(value_error_message="Error: Not enough arguments. Usage: search-address [search term]")
def search_by_address(args, book: AddressBook):
    search_term = ' '.join(args).lower()
    matching_contacts = []

    for record in book.data.values():
        if record.address and search_term in str(record.address).lower():
            matching_contacts.append(record)

    if not matching_contacts:
        return "No contacts found with this address."

    pretty_records(matching_contacts)

    return ""


@command_check_decorator(
    index_error_message="Error: Not enough arguments. Usage: remove-address [name]"
)
def remove_address(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record is None or not record.address:
        return f"No address found for contact '{name}'"
    record.remove_address()
    return "Address removed."

@command_check_decorator(
        index_error_message="Error: Not enough arguments. Usage: contacts-birthdays-within [birthdays-days-within]"
        )
def show_contacts_birthdays_within(args, book: AddressBook):
    days_till = args[0]
    result = book.get_birthdays_till_date(int(days_till))
    return result 
