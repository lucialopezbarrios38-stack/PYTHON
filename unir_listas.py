cantidad = int(input("Cantidad de elementos: "))

lista1 = []
lista2 = []
lista_combinada = []

print("Lista 1:")

for i in range(cantidad):
    numero = int(input("Ingrese un número: "))
    lista1.append(numero)

print("Lista 2:")

for i in range(cantidad):
    numero = int(input("Ingrese un número: "))
    lista2.append(numero)

lista_combinada = lista1 + lista2

print("Lista combinada:")

for numero in lista_combinada:
    print(numero)