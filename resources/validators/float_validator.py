def discount_validator(discount_str):
    if discount_str.strip() == "":
        return 0.0
    else:
        try:
            return float(discount_str)
        except ValueError:
            return 0.0