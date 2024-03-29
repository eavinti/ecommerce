from resources.enums.promotional_code_enum import DiscountType, PurchaseType, CouponScope

from typing import Optional
from models.promotional_code import PromotionalCode

class Cart:
    def __init__(self, country):
        self.country = country
        self.items = []
        self.promotional_code: Optional[PromotionalCode] = None  # Type hint que indica que puede ser PromotionalCode o None

    def add_item(self, item, amount):
        """Añade un producto al carro"""
        amount = float(amount)
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
        return total

    def check_item_rule(self, value, item_total_without_discount):
        is_active = False
        if self.promotional_code.purchase_type == PurchaseType.TOTAL.value and self.promotional_code.minimum_purchase < item_total_without_discount < self.promotional_code.maximum_purchase:
            is_active = True
        if self.promotional_code.purchase_type == PurchaseType.AMOUNT.value and self.promotional_code.minimum_purchase < value['amount'] < self.promotional_code.maximum_purchase:
            is_active = True
        return is_active

    def check_cart_rule(self, total):
        is_active = False
        if self.promotional_code.minimum_purchase < total < self.promotional_code.maximum_purchase:
            is_active = True
        return is_active

    def get_invoice(self):
        total = 0
        total_with_discount = 0
        items = []
        if len(self.items) == 0:
            return total, total_with_discount, items

        code = self.promotional_code
        code_scope = None
        code_item = None
        code_discount_type = None
        purchase_type = None
        correct_rule = False
        if code:
            code_scope = code.scope
            code_discount_type = code.discount_type
            purchase_type = code.purchase_type
            if code_scope == CouponScope.ITEM.value:
                code_item = code.item
            if purchase_type == PurchaseType.TOTAL.value:
                pass
            if purchase_type == PurchaseType.AMOUNT.value:
                pass

        for value in self.items:
            item_total_without_discount = value['item'].final_price(self.country) * float(value['amount'])
            item_total_with_discount = item_total_without_discount
            if code and code_scope == CouponScope.ITEM.value and code_item and code_item == value['item'].id:
                rule = self.check_item_rule(value, item_total_without_discount)
                if rule:
                    if code_discount_type == DiscountType.FIXED_DISCOUNT.value:
                        item_total_with_discount = item_total_without_discount - code.discount_value
                    if code_discount_type == DiscountType.PERCENTAGE_DISCOUNT.value:
                        item_total_with_discount = item_total_without_discount - (item_total_without_discount * (code.discount_value / 100))

            items.append({
                'id': value['item'].id,
                'title': value['item'].title,
                'price': value['item'].prices[self.country],
                'discount': value['item'].discounts[self.country],
                'amount': value['amount'],
                'final_price': value['item'].final_price(self.country),
                'total': item_total_without_discount,
                'total_with_discount': item_total_with_discount,
            })
            total += item_total_without_discount
            total_with_discount += item_total_with_discount

        if code and code_scope == CouponScope.CART.value:
            cart_rule = self.check_cart_rule(total)
            if cart_rule:
                if code_discount_type == DiscountType.FIXED_DISCOUNT.value:
                    total_with_discount = total - code.discount_value
                if code_discount_type == DiscountType.PERCENTAGE_DISCOUNT.value:
                    total_with_discount = total - (total * (code.discount_value / 100))

        return total, total_with_discount, items
