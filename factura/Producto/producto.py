inventario = { "piña": {"stock": 10, "precio": 5.00}, 
              "lapiz": {"stock": 20, "precio": 3.50},
              "melon": {"stock": 15, "precio": 7.25} }

def mostrar_stock(): 
    print("\nStock Actual:") 
    for producto, detalles in inventario.items(): 
        print(f"{producto}: {detalles['stock']} unidades disponibles")
