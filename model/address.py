import re
from .field import Field


# Збереження та валідація адреси
class Address(Field):
    def __init__(self, value):
        if not self.validate_address(value):
            raise ValueError("Invalid address format")
        super().__init__(value)

    @staticmethod
    def validate_address(value):
        # Вулиця, пробіл, номер будинку, кома та пробіл, індекс та місто, кома та пробіл, країна
        pattern = r'^[A-Za-z\s]+ \d+, \d{5} [A-Za-z\s]+, [A-Za-z\s]+$' 
        return bool(re.match(pattern, value))

