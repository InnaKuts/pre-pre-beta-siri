from ..model.field import Field


class Tags(Field):
    def __init__(self, value: [str]):
        super().__init__(set(value))

    def add(self, tag: str):
        self.value.add(tag)

    def remove(self, tag: str):
        self.value.remove(tag)

    def clear(self):
        self.value.clear()

    def has(self, other: list[str], match_all: bool = False):
        return self.has_all(other) if match_all else self.has_any(other)

    def has_any(self, other: list[str]):
        return len(self.value.intersection(other)) > 0

    def has_all(self, other: list[str]):
        return self.value.issuperset(other)

    def __len__(self):
        return len(self.value)

    def __contains__(self, item: str):
        return item in self.value

    def __iter__(self):
        return iter(self.value)
