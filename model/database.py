from model.addressBook import AddressBook
from notes.notebook import Notebook

class Database:
    Default = None

    def __init__(self, address_book, notebook):
        self.address_book = address_book
        self.notebook = notebook

Database.Default = Database(AddressBook(), Notebook())
