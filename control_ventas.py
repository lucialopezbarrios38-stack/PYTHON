cantidad = int(input("Cantidad de vendedores: "))

ventas = {}

for i in range(cantidad):
    nombre = input("Nombre del vendedor: ")
    total = float(input("Total vendido: "))

    ventas[nombre] = total

mejor_vendedor = ""
mayor_venta = 0

for nombre, total in ventas.items():
    if total > mayor_venta:
        mayor_venta = total
        mejor_vendedor = nombre

print("Mayor vendedor:")
print(mejor_vendedor, "-> $", int(mayor_venta))