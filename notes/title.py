from model.field import Field


class Title(Field):
    __words: set = None

    def __init__(self, value):
        if not value:
            raise Exception("Title can't be empty")
        super().__init__(str(value))
        self.__words = self.__calc_words()

    @property
    def words(self):
        if not self.__words:
            self.__words = self.__calc_words()
        return self.__words

    def __calc_words(self):
        return {w.strip().lower() for w in self.value.split()}

    def has(self, other: list[str], match_all: bool = False):
        return self.has_all(other) if match_all else self.has_any(other)

    def has_any(self, other: list[str]):
        return len(self.words.intersection(other)) > 0

    def has_all(self, other: list[str]):
        return self.words.issuperset(other)
