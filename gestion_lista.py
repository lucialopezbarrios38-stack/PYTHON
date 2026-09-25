cantidad = int(input("Cantidad de productos: "))

productos = []

for i in range(cantidad):
    producto = input("Ingrese un producto: ")
    productos.append(producto)

print("Lista de compras:")

for i in range(cantidad):
    print(i + 1, ".", productos[i])