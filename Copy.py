from Stock import stock as  st



producto_solicitado = input("Ingresa el nombre del producto que deseas pedir: ")
cantidad_solicitada = int(input("Ingresa la cantidad que deseas pedir: "))

st.pedir_producto(producto_solicitado, cantidad_solicitada)