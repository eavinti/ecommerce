from resources.validators.float_validator import discount_validator

from models.item import Item


def list_item(items):
    print("---------------------------------------")
    print("PRODUCTOS: ")
    print(f"{'ID':<{20}} {'TITLE':<{20}} {'PRICES':<{45}} {'DISCOUNTS':<{45}}")
    for key, item in items.items():
        print(f"{key:<{20}}{item.title:<{20}} {str(item.prices):<{45}} {str(item.discounts):<{45}}")
    print("---------------------------------------")

def create_item():
    title = input("Nombre del producto: ")
    price_es = float(input("Precio en España: "))
    price_gb = float(input("Precio en GB: "))
    price_it = float(input("Precio en Italia: "))
    discount_es = discount_validator(input("Descuento en España (%) [0%]: "))
    discount_gb = discount_validator(input("Descuento en GB (%) [0%]: "))
    discount_it = discount_validator(input("Descuento en Italia (%)[0%]: "))
    return Item(
        title,
        {"ES": price_es, "GB": price_gb, "IT": price_it},
        {"ES": discount_es, "GB": discount_gb, "IT": discount_it}
    )