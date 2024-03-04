class PromotionalCode:
    def __init__(self, code, discount, minimum_purchase):
        """
        - code: str
        - discount: float, cantidad fija a descontar
        - minimum_purchase: float, mínimo necesario para aplicar el descuento
        """
        self.code = code
        self.discount = discount
        self.minimum_purchase = minimum_purchase

    def apply_discount(self, cart_total):
        """Verifica si el descuento puede aplicarse al total actual del carro."""
        return cart_total >= self.minimum_purchase