from models.cart import Cart


def cart_total(cart):
    if isinstance(cart, Cart):
        total, total_with_discount, items = cart.get_invoice()
        cart_country = cart.country
        print('----------------------------------------------')
        print('Carro de compras 🛒:')
        print('El carro de compras se inicio con país 🌎: {}'.format(cart_country))
        if cart.promotional_code:
            print('Tiene un código promocional 🎫: {}'.format(cart.promotional_code.code))
        print('')
        print(
            f"{'ID':<{20}}{'TÍTULO':<{20}}{'PRECIO':<{20}}{'DESCUENTO (%)':<{20}}{'CANTIDAD':<{20}}{'PRECIO FINAL':<{20}}{'TOTAL':<{20}}{'TOTAL CON DESCUENTO':<{20}}")
        for item in items:
            print(
                f"{item['id']:<{20}}{item['title']:<{20}}{item['price']:<{20}}{item['discount']:<{20}}{item['amount']:<{20}}{item['final_price']:<{20}}{item['total']:<{20}.2f}{item['total_with_discount']:<{20}.2f}"
            )

        print('')
        print(f"Total sin descuentos: {total:.2f}€")
        print(f"Total con descuentos: {total_with_discount:.2f}€")
        print('----------------------------------------------')
        return True
    print('- :( el carro sigue vacio.')
    return False
