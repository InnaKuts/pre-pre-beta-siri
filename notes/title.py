from model.field import Field


class Title(Field):
    def __init__(self, value):
        if not value:
            raise Exception("Title can't be empty")
        super().__init__(str(value))

    def has(self, other: list[str]):
        for key in other:
            if key in self.value:
                return True
        return False
