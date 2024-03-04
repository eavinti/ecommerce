from models.item import Item
from models.promotional_code import PromotionalCode
from models.cart import Cart

from resources.test_data import ITEMS
from controllers.item_controller import list_item, create_item
from controllers.cart_controller import cart_total


def main():
    items = {}  # Diccionario para almacenar los productos disponibles
    promotional_codes = {}  # Diccionario para almacenar los códigos promocionales
    current_cart = None
    test_data_used = False

    while True:
        print("\nComandos disponibles:")
        print("1. Añadir producto al catálogo")
        print("2. Mostrar productos disponibles")
        print("3. Añadir producto al carro")
        print("4. Aplicar código promocional")
        print("5. Mostrar total del carro")
        print("6. Agrega datos de prueba")
        print("7. Salir")
        option = input("Seleccione una opción: ")

        if option == "1":
            item = create_item()
            items[item.id] = item
        elif option == "2":
            list_item(items)
        elif option == "3":
            if not isinstance(current_cart, Cart):
                country = input("¿De qué país estás comprando? (ES, GB, IT): ")
                current_cart = Cart(country)
            item_id = input("Ingresa el ID del producto: ")
            amount = input("Ingresa la cantidad del producto: ")
            if item_id in items:
                current_cart.add_item(items[item_id], amount)
            else:
                print("Producto no encontrado.")
        elif option == "4":
            code = input("Introduce el código promocional: ")
            if code in promotional_codes:
                current_cart.apply_promotional_code(promotional_codes[code])
            else:
                print("Código promocional no encontrado.")
        elif option == "5":
            cart_total(current_cart)
        elif option == "6":
            for test_item in ITEMS:
                items[test_item.id] = test_item
            list_item(items)
        elif option == "7":
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
