import unittest
from models.item import Item

class TestItem(unittest.TestCase):
    def setUp(self):
        self.prices = {'ES': 100, 'IT': 120}
        self.discounts = {'ES': 10, 'IT': 0}  # 10% de descuento en ES,
        self.item = Item("Test Item", self.prices, self.discounts)

    def test_final_price_without_discount(self):
        """Probar que el precio final es correcto sin aplicar descuento."""
        # IT no tiene descuento
        self.assertEqual(self.item.final_price('IT'), 120)

    def test_final_price_with_discount(self):
        """Probar que el precio final es correcto después de aplicar el descuento."""
        # ES tiene un descuento del 10%
        expected_price = 100 - (100 * 10 / 100)  # Precio esperado después del descuento
        self.assertEqual(self.item.final_price('ES'), expected_price)

if __name__ == '__main__':
    unittest.main()