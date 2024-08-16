from .address import Address
from .name import Name
from .phone import Phone
from .birthday import Birthday
from datetime import datetime, timedelta

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.email = None
        self.address = None

    def __str__(self):
        phones = '; '.join(ph.value for ph in self.phones)
        birthday_str = self.birthday.value.strftime('%d.%m.%Y') if self.birthday else 'N/A'
        address_str = f", address: {self.address}" if self.address else ""
        return f"Contact name: {self.name.value}, phones: {phones}, birthday: {birthday_str}{address_str}"
    
    def add_phone(self, phone:str):
        for ph in self.phones:
            if(ph.value == phone):
                return
        self.phones.append(Phone(phone))

    def remove_phone(self, phone:str):
        ph = self.find_phone(phone) 
        index_to_delete = self.phones.index(ph) 
        self.phones.pop(index_to_delete)

    def edit_phone(self, old_phone:str, new_phone:str):
        for ind, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[ind] = Phone(new_phone)
                return
        raise Exception(f"No {old_phone} phone found for {self.name.value}")
    
    def find_phone(self, phone:str):
        for  ph in self.phones:
            if phone == ph.value:
                return ph
        raise Exception(f"No {phone} phone found for {self.name.value}")

    def add_birthday(self, birthday):
        datetime_birthday = Birthday(birthday)
        if datetime_birthday.value > datetime.today().date():
            raise Exception("Birthday can't be in the future")
        if datetime_birthday.value < datetime.today().date() - timedelta(days=365 * 150):
            raise Exception("Birthday can't be more than 150 years ago")
        self.birthday = datetime_birthday

    def delete_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def add_email(self, email):
        self.email = email

    def edit_email(self, new_email):
        self.email = new_email

    def delete_email(self):
        self.email = None

    def add_address(self, address: str):
        self.address = Address(address)

    def edit_address(self, address: str):
        self.address = Address(address)

    def remove_address(self):
        self.address = None
