import re
from .field import Field


class Address(Field):
    def __init__(self, value):
        if not self.validate_address(value):
            raise ValueError("Invalid address format")
        super().__init__(value)

    @staticmethod
    def validate_address(value):
        
        pattern = r'^[A-Za-z\s]+ \d+, \d{5} [A-Za-z\s]+, [A-Za-z\s]+$' 
        return bool(re.match(pattern, value))
    





