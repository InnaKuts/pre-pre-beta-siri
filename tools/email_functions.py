
from model.addressBook import AddressBook
from tools import command_check_decorator


def email_validator(func):
    def wrapper(*args, **kwargs):
        email = args[0][1]  # Assuming email is always the second argument
        if "@" not in email or "." not in email:
            return "Error: Invalid email format."
        return func(*args, **kwargs)
    return wrapper

@email_validator
@command_check_decorator(
        value_error_message="Error: Not enough arguments. Usage: add-email [name] [email]"
        )
def add_email(args, book: AddressBook):
    name, email, *_ = args
    record = book.find(name)
    if record is None:
        raise Exception(f"No '{name}' contact found")
    record.add_email(email)
    return "Email added."

@command_check_decorator(
        index_error_message="Error: Not enough arguments. Usage: show-email [name]",
        key_error_message= "Error: Contact not found"
        )
def show_email(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record is None:
        raise Exception(f"No '{name}' contact found")
    return record.email

@email_validator
@command_check_decorator(
        value_error_message="Error: Not enough arguments. Usage: change-email [name] [new email]"
        )
def change_email(args, book: AddressBook):
    name, new_email, *_ = args
    record = book.find(name)
    if record is None:
        raise Exception(f"No '{name}' contact found")
    record.edit_email(new_email)
    return "Email updated."

@command_check_decorator(
        value_error_message="Error: Not enough arguments. Usage: delete-email [name]"
        )
def delete_email(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record is None:
        raise Exception(f"No '{name}' contact found")
    record.delete_email()
    return "Email removed."