from resources.enums.promotional_code_enum import DiscountType, PurchaseType, CouponScope

from models.item import Item
from models.promotional_code import PromotionalCode

ITEMS = [
    Item(
        "Camiseta A",
        {"ES": "15", "GB": "17", "IT": "19"},
        {"ES": "15", "GB": "20", "IT": "25"}
    ),
    Item(
        "Pantalon A",
        {"ES": "35", "GB": "37", "IT": "39"},
        {"ES": "8", "GB": "16", "IT": "24"}
    ),
    Item(
        "Bufanda A",
        {"ES": "8", "GB": "7", "IT": "9"},
        {"ES": "5", "GB": "7", "IT": "10"}
    )
]


def create_coupons(item_id):
    promotional_codes = [
        PromotionalCode(
            code='PROMO10',
            discount_value=10,
            discount_type=DiscountType.PERCENTAGE_DISCOUNT.value,
            scope=CouponScope.ITEM.value,
            item=item_id,
            purchase_type=PurchaseType.AMOUNT.value,
            minimum_purchase=100,
            maximum_purchase=150
        ),
        PromotionalCode(
            code='PROMO50',
            discount_value=50,
            discount_type=DiscountType.FIXED_DISCOUNT.value,
            scope=CouponScope.CART.value,
            purchase_type=PurchaseType.AMOUNT.value,
            minimum_purchase=200,
            maximum_purchase=500
        ),
    ]
    return promotional_codes
