from resources.enums.country_enum import Country


def country_validator(country_code):
    if country_code.strip() == "" and not Country.has_value(country_code):
        return Country.SPAIN.value
    return country_code

