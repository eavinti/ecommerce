from resources.enums.country_enum import Country
from resources.enums.promotional_code_enum import DiscountType, PurchaseType, CouponScope


def country_validator(country_code):
    if country_code.strip() == "" and not Country.has_value(country_code):
        return Country.SPAIN.value
    return country_code

def discount_type_validator(discount_type):
    if discount_type in ('fijo', 'porcentaje'):
        if discount_type == 'fijo':
            return DiscountType.FIXED_DISCOUNT.value
        if discount_type == 'porcentaje':
            return DiscountType.PERCENTAGE_DISCOUNT.value
    else:
        return DiscountType.PERCENTAGE_DISCOUNT.value


def coupon_scope_validator(coupon_scope):
    if coupon_scope in ('carrito', 'producto'):
        if coupon_scope == 'carrito':
            return CouponScope.CART.value
        if coupon_scope == 'producto':
            return CouponScope.ITEM.value
    else:
        return CouponScope.CART.value


def purchase_type_validator(purchase_type):
    if purchase_type in ('cantidad', 'total'):
        if purchase_type == 'cantidad':
            return PurchaseType.AMOUNT.value
        if purchase_type == 'total':
            return PurchaseType.TOTAL.value
    else:
        return PurchaseType.TOTAL.value
