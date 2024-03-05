from typing import Optional
from models.promotional_code import PromotionalCode

class Cart:
    def __init__(self, country):
        self.country = country
        self.items = []
        self.promotional_code: Optional[PromotionalCode] = None  # Type hint que indica que puede ser PromotionalCode o None

    def add_item(self, item, amount):
        """Añade un producto al carro, considerando el país para el precio."""
        self.items.append({'item': item, 'amount': amount})

    def apply_promotional_code(self, code):
        """Aplica un código promocional al carro."""
        self.promotional_code = code

    def cart_total(self):
        """Calcula el total del carro aplicando descuentos de productos y códigos promocionales."""
        total = 0
        if len(self.items) == 0:
            return total
        for value in self.items:
            item = value['item']
            amount = float(value['amount'])
            final_price = item.final_price('ES')


            total += (final_price * amount)
        # total = sum(item.final_price(country) for item, country in self.items)
        #
        # # Aplicar descuento de código promocional si existe
        # if self.promotional_code and self.promotional_code.apply_discount(total):
        #     total -= self.promotional_code.discount
        #
        return total
