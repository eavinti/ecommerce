from resources.validators.float_validator import float_validator
from resources.validators.string_validator import discount_type_validator, purchase_type_validator, \
    coupon_scope_validator

from resources.enums.promotional_code_enum import DiscountType, CouponScope, PurchaseType

from models.promotional_code import PromotionalCode


def create_coupon():
    print("Nuevo código promocional")
    code = input("Código promocional (promo100): ")
    discount_value = float_validator(input("Cantidad a descontar (10): "))

    discount_type = discount_type_validator(input("Tipo de descuento (fijo - porcentaje): "))
    discount_type_char = '%' if discount_type == DiscountType.PERCENTAGE_DISCOUNT.value else '€'
    print('El valor a descontar del código promocional es de {} {}'.format(discount_value, discount_type_char))

    print("¿El código promocional es para todo el carrito o solo para un producto?")
    scope = coupon_scope_validator(input("Alcance (carrito - producto): "))
    item = None
    if scope == CouponScope.ITEM.value:
        print("¿Qué producto se descuenta con este cupón?")
        item = input("Código del poducto: ")

    print("¿El descuento se aplica por una cantidad de productos, o por un valor total?")
    total_type = purchase_type_validator(input("Tipo de total (cantidad - total): "))

    minimum_purchase = float_validator(input("Mínimo necesario para aplicar el descuento: "))
    maximum_purchase = float_validator(input("Máximo necesario para aplicar el descuento: "))

    coupon = PromotionalCode(
        code=code,
        discount_value=discount_value,
        discount_type=discount_type,
        scope=scope,
        item=item,
        purchase_type=total_type,
        minimum_purchase=minimum_purchase,
        maximum_purchase=maximum_purchase,
    )

    will_be_applied_in = 'todo el carrito' if scope == CouponScope.CART.value else "el producto '{}'".format(item)
    total_type_discount = 'unidades compradas' if total_type == PurchaseType.AMOUNT.value else '€ comprados'
    print(
        "- 🔥 el codigo promocional '{}' tiene un descuento de {} {}, se aplicará en {}. Será válido si cumple de {} a {} {}.".format(
            code,
            discount_value,
            discount_type_char,
            will_be_applied_in,
            minimum_purchase,
            maximum_purchase,
            total_type_discount,
        )
    )
    return coupon


def list_coupons(coupons):
    print("---------------------------------------")
    print("CÓDIGOS PROMOCIONALES: ")
    for coupon in coupons.values():
        discount_type_char = '%' if coupon.discount_type == DiscountType.PERCENTAGE_DISCOUNT.value else '€'
        will_be_applied_in = 'todo el carrito' if coupon.scope == CouponScope.CART.value else "el producto '{}'".format(
            coupon.item)
        total_type_discount = 'unidades compradas' if coupon.purchase_type == PurchaseType.AMOUNT.value else '€ comprados'
        print(
            "- 🎫 '{}': tiene un descuento de {} {}, se aplicará en {}. Será válido si cumple de {} a {} {}.".format(
                coupon.code,
                coupon.discount_value,
                discount_type_char,
                will_be_applied_in,
                coupon.minimum_purchase,
                coupon.maximum_purchase,
                total_type_discount,
            )
        )
    print("---------------------------------------")
