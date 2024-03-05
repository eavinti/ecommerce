import unittest

from models.item import Item
from models.cart import Cart

from models.promotional_code import PromotionalCode, DiscountType, PurchaseType, CouponScope


class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = Cart('ES')
        self.item1 = Item("Producto1", {'ES': 100}, {'ES': 10})  # Precio 100, Descuento 10%
        self.item2 = Item("Producto2", {'ES': 200}, {'ES': 0})  # Precio 200, sin descuento

    def test_add_item(self):
        """Prueba añadir un producto al carrito."""
        self.cart.add_item(self.item1, 1)
        self.assertEqual(len(self.cart.items), 1)

    def test_cart_total_without_discount(self):
        """Prueba el total del carrito sin descuento."""
        self.cart.add_item(self.item1, 1)
        self.cart.add_item(self.item2, 1)
        self.assertEqual(self.cart.cart_total(), 290)

    def test_cart_total_with_promotional_code(self):
        """Prueba el total del carrito con un código promocional aplicado."""
        self.cart.add_item(self.item1, 2)  # Total sin descuento sería 200
        promotional_code = PromotionalCode(
            "PROMO10", 10, DiscountType.PERCENTAGE_DISCOUNT, CouponScope.CART,
            purchase_type=PurchaseType.TOTAL
        )
        self.cart.apply_promotional_code(promotional_code)
        # lógica para aplicar correctamente el descuento
        total, total_with_discount, items = self.cart.get_invoice()
        expected_discounted_total = 200 - (200 * 0.1)  # Descuento del 10%
        self.assertEqual(total_with_discount, expected_discounted_total)


if __name__ == '__main__':
    unittest.main()
