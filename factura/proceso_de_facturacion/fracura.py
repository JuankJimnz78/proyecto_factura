
def imprimir_factura(nombre, apellido, cedula, producto, cantidad, precio_unitario, subtotal, iva, total):
    print("\n*** Factura ***")
    print(f"El nombre del cliente es: {nombre}")
    print(f"Su apellido es: {apellido}")
    print(f"Su cédula es: {cedula}")
    print(f"Producto: {producto}")
    print(f"Cantidad: {cantidad}")
    print(f"Precio Unitario: ${precio_unitario:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"IVA (15%): ${iva:.2f}")
    print(f"Total: ${total:.2f}")
    print("****************\n")
