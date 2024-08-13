import time
from .contact import Contact
from .description import Description
from .tags import Tags
from .title import Title


class Note:
    def __init__(self, title: str, description: str, contact: str = None, tags: [str] = None):
        self.__uuid = str(time.time())
        self.contact = Contact(contact) if contact else None
        self.title = Title(title)
        self.description = Description(description)
        self.tags = Tags(tags or [])

    @property
    def uuid(self):
        return self.__uuid

    def __str__(self):
        return f"Title: {self.title}, note: {repr(self.description)}, contact: {self.contact or '<N/A>'}, tags: {';'.join(self.tags)}"
