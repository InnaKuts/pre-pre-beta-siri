from model.field import Field


class Description(Field):
    def __init__(self, value):
        if not value:
            raise Exception("Description can't be empty")
        super().__init__(str(value))
