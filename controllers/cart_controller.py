from resources.validators.string_validator import country_validator
from models.cart import Cart


def cart_total(cart):
    total = 0
    if isinstance(cart, Cart):
        total = cart.cart_total()
    print(f"Total del carro: {total}€")


# def add_product_to_cart(cart, items):
#     if not isinstance(cart, Cart):
#         country = country_validator(input("¿De qué país estás comprando? (ES, GB, IT): "))
#         cart = Cart(country)
#     item_id = input("Ingresa el ID del producto: ")
#     amount = input("Ingresa la cantidad del producto: ")
#     if item_id in items:
#         cart.add_item(items[item_id], amount)
#     else:
#         print("Producto no encontrado.")