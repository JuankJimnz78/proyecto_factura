from Stock import stock as  st
from Producto import producto as pr
usuarios = { "cliente1": "password1", "cliente2": "password2"}



def verificar_usuario(nombre, contrasena):
    if nombre in usuarios and usuarios[nombre] == contrasena:
        return True
    return False



def mostrar_menu():
    print("Menú Principal")
    print("1. Pedir Producto")
    print("2.Ver stock")
    print("3. Salir")

def iniciar_sesion(nombre,contrasena):
    
    if verificar_usuario(nombre, contrasena):
        print(f"Bienvenido, {nombre}!")
        while True:
            mostrar_menu()
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                st.pedir_producto()
            elif opcion == "2":
                pr.mostrar_stock()
            elif opcion == "3":
                print("Muchas gracias por la compra...")
                break
            
            else:
                print("Opción no válida, por favor intente de nuevo.")
    else:
        print("Nombre o contraseña incorrectos.")

        
nombre_usuario = input("Ingrese su nombre: ")
contrasena_usuario = input("Ingrese su contraseña: ")
                         

iniciar_sesion(nombre_usuario,contrasena_usuario)
