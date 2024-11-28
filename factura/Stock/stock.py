from Producto import producto as proc
from proceso_de_facturacion import fracura as fac

# Información del cliente



"""def pedir_producto(producto, cantidad_pedida):
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    cedula = input("Ingresa tu cédula: ")
    if producto in proc.inventario:
        if proc.inventario[producto]["stock"] >= cantidad_pedida:
            proc.inventario[producto]["stock"] -= cantidad_pedida
            precio_unitario = proc.inventario[producto]["precio"]
            subtotal = precio_unitario * cantidad_pedida
            iva = subtotal * 0.15
            total = subtotal + iva
            print(f"Has pedido {cantidad_pedida} unidades de {producto}.")
            print(f"Quedan {proc.inventario[producto]['stock']} unidades de {producto} en stock.")
            fac.imprimir_factura(nombre, apellido, cedula, producto, cantidad_pedida, precio_unitario, subtotal, iva, total)
        else:
            print(f"No hay suficiente stock de {producto} para pedir {cantidad_pedida} unidades.")
    else:
        print(f"El producto {producto} no existe en el inventario.")"""

def pedir_producto():
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    cedula = input("Ingresa tu cédula: ")
    producto = input("Ingrese el nombre del producto: ")
    cantidad_pedida = int(input("Ingrese la cantidad deseada: "))
    
    if producto in proc.inventario:
        if proc.inventario[producto]["stock"] >= cantidad_pedida:
            proc.inventario[producto]["stock"] -= cantidad_pedida
            precio_unitario = proc.inventario[producto]["precio"]
            subtotal = precio_unitario * cantidad_pedida
            iva = subtotal * 0.15
            total = subtotal + iva
            print(f"Has pedido {cantidad_pedida} unidades de {producto}.")
            print(f"Quedan {proc.inventario[producto]['stock']} unidades de {producto} en stock.")
            fac.imprimir_factura(nombre, apellido, cedula, producto, cantidad_pedida, precio_unitario, subtotal, iva, total)
        else:
            print(f"No hay suficiente stock de {producto} para pedir {cantidad_pedida}")
            print(f"Quedan {proc.inventario[producto]['stock']} unidades de {producto} en stock.")
                  
    else:
        print(f"El producto {producto} no existe en el inventario.")



