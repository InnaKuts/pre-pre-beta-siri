"""
Скрипт генерації тестових даних.
"""
from ..model import Address, AddressBook, Birthday, Phone, Record
from ..tools import command_check_decorator


@command_check_decorator()
def add_test_data(args, book: AddressBook):

    for test_record in generate_test_data():
        if test_record.name in book:
            continue
        book.add_record(test_record)
    return "Test data added"


def generate_test_data():
    test_records = [
        Record(name="John"),  # Shared phone, unique email
        Record(name="Jane"),  # Shared phone
        Record(name="Emily"),  # Shared address
        Record(name="Michael"),  # Shared address, unique phone
        Record(name="Sam"),  # Unique email
    ]

    # Adding shared and unique fields
    test_records[0].phones.append(Phone("1234567890"))  # Shared phone
    test_records[0].email = "john.doe@example.com"  # Unique email

    test_records[1].phones.append(Phone("1234567890"))  # Shared phone
    test_records[1].email = "shared@example.com"  # Shared email
    test_records[1].address = Address("Main St 123, 11111 CA, US")  # Shared address

    test_records[2].phones.append(Phone("9876543210"))  # Unique phone
    test_records[2].address = Address("Main St 123, 11111 CA, US")  # Shared address

    test_records[3].phones.append(Phone("5551234567"))  # Unique phone
    test_records[3].address = Address("Oak Rd 456, 11111 NY, US")  # Shared address
    test_records[3].birthday = Birthday("30.08.2000")

    test_records[4].phones.append(Phone("1234567890"))  # Shared phone
    test_records[4].email = "sam.brown@uniquemail.com"  # Unique email

    return test_records
