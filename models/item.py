from resources.helpers.string_helper import get_random_string


class Item:
    def __init__(self, title, prices, discounts=None):
        """
        - title: str
        - price: dict, {código_país: precio}
        - discounts: dict, {código_país: descuento}, el descuento es un porcentaje (ej. 10 para 10%)
        """
        self.id = get_random_string()
        self.title = title
        self.prices = prices
        self.discounts = discounts if discounts else {}

    def final_price(self, pais):
        """Calcula el precio final del producto después de aplicar el descuento."""
        base_price = float(self.prices[pais])
        discount = float(self.discounts.get(pais, 0))
        if discount == 0:
            return base_price
        return base_price - (base_price * discount / 100)