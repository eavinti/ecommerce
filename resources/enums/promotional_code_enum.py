from enum import Enum


class DiscountType(Enum):
    FIXED_DISCOUNT = 'fixed_discount'
    PERCENTAGE_DISCOUNT = 'percentage_discount'

    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)


class PurchaseType(Enum):
    AMOUNT = 'amount'
    TOTAL = 'total'

    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)


class CouponScope(Enum):
    CART = "cart"
    ITEM = "item"

    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)