from models.cart import Cart


def cart_total(cart):
    if isinstance(cart, Cart):
        total = cart.cart_total()
        cart_country = cart.country
        print('----------------------------------------------')
        print('Carro de compras 🛒:')
        print('El carro de compras se inicio con país 🌎: {}'.format(cart_country))
        if cart.promotional_code:
            print('Tiene un código promocional 🎫: {}'.format(cart.promotional_code.code))
        print('')
        print(f"{'ID':<{20}} {'TÍTULO':<{20}} {'PRECIO':<{20}} {'DESCUENTO (%)':<{20}} {'CANTIDAD':<{20}} {'PRECIO FINAL':<{20}} {'TOTAL':<{20}}")
        for value in cart.items:
            item_total = value['item'].final_price(cart_country) * float(value['amount'])
            print(
                f"{value['item'].id:<{20}}{value['item'].title:<{20}} {value['item'].prices[cart_country]:<{20}} {value['item'].discounts[cart_country]:<{20}} {value['amount']:<{20}} {value['item'].final_price(cart_country):<{20}} {item_total:<{20}}"
            )

        print(f"Total sin descuentos carro: {total}€")
        print('----------------------------------------------')
        return True
    print('- :( el carro sigue vacio.')
    return False

