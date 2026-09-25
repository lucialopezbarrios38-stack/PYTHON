cantidad = int(input("Cantidad de productos: "))

inventario = {}

for i in range(cantidad):
    producto = input("Producto: ")
    cantidad_producto = int(input("Cantidad: "))

    inventario[producto] = cantidad_producto

buscar = input("Consultar producto: ")

if buscar in inventario:
    print("Cantidad disponible de", buscar + ":", inventario[buscar])
else:
    print("El producto no existe.")