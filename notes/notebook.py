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

    def find_notes(self, tags: [str], match_all: bool = False):
        return [d for d in self.data if d.tags.has(tags, match_all)]

