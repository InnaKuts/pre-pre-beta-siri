from functools import reduce

from model.field import Field


class Description(Field):
    def __init__(self, value):
        if not value:
            raise Exception("Description can't be empty")
        super().__init__(str(value))

    def __repr__(self):
        return repr(self.value)

    def has(self, other: list[str], match_all: bool):
        if match_all:
            return reduce(lambda acc, e: acc and e in self.value, other, True)
        else:
            return reduce(lambda acc, e: acc or e in self.value, other, False)
