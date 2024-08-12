from model.field import Field


class Title(Field):
    def __init__(self, value):
        if not value:
            raise Exception("Title can't be empty")
        super().__init__(str(value))
