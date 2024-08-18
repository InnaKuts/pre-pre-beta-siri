"""
Модель для роботи з блокнотом, який містить нотатки.
"""
from collections import UserDict

from .note import Note


class Notebook(UserDict):
    def add_note(self, note: Note):
        if note.uuid not in self.data:
            self.data[note.uuid] = note
            return True
        return False

    def update_note(self, note: Note):
        if note.uuid in self.data:
            self.data[note.uuid] = note
            return True
        return False

    def delete_note(self, uuid: str):
        if uuid in self.data:
            del self.data[uuid]
            return True
        return False

    def find_notes_by_title(self, words: [str], match_all: bool = False):
        return [d for d in self.data.values() if d.title.has(words, match_all)]

    def find_notes_by_tags(self, tags: [str], match_all: bool = False):
        return [d for d in self.data.values() if d.tags.has(tags, match_all)]

    def find_notes_by_description(self, words: [str], match_all: bool = False):
        return [d for d in self.data.values() if d.description.has(words, match_all)]
