from enum import Enum

# class syntax
class Country(Enum):
    SPAIN = 'ES'
    UNITED_KINGDOM = 'GB'
    ITALY = 'IT'

    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)