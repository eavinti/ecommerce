from resources.enums.promotional_code_enum import DiscountType, PurchaseType, CouponScope


class PromotionalCode:
    def __init__(
            self,
            code:str,
            discount_value: float = 0,
            discount_type: DiscountType = DiscountType.PERCENTAGE_DISCOUNT.value,
            scope: CouponScope = CouponScope.CART.value,
            item: str = None,
            purchase_type: PurchaseType = PurchaseType.AMOUNT.value,
            minimum_purchase:float=0,
            maximum_purchase:float=0,
    ):
        """
        - code: str
        - discount_value: float, cantidad a descontar
        - discount_type: DiscountType, FIXED_DISCOUNT= descuento fijo y PERCENTAGE_DISCOUNT = descuento de porcentaje
        - scope: CouponScope, Si el descuento es el carrito a un producto en especifico
        - item: str, code del producto
        - # REGLA SI CUMPLE EL DESCUENTO:
        - purchase_type: PurchaseType,
        - minimum_purchase: float, mínimo necesario para aplicar el descuento
        - maximum_purchase: float, máximo necesario para aplicar el descuento
        """

        if scope == CouponScope.ITEM.value and not item:
            raise ValueError("Se debe proporcionar el código del PRODUCTO cuando el scope es 'ITEM'.")

        self.code = code
        self.discount_value = discount_value
        self.discount_type = discount_type
        self.scope = scope
        self.item = item
        self.purchase_type = purchase_type
        self.minimum_purchase = minimum_purchase
        self.maximum_purchase = maximum_purchase

    def apply_discount(self, cart_total):
        """Verifica si el descuento puede aplicarse al total actual del carro."""
        # TODO fixit
        return cart_total >= self.minimum_purchase

