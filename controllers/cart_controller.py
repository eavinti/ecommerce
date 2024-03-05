from resources.validators.string_validator import country_validator
from models.cart import Cart


def cart_total(cart):
    total = 0
    if isinstance(cart, Cart):
        total = cart.cart_total()
    print(f"Total del carro: {total}€")


