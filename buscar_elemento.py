cantidad = int(input("Cantidad de números: "))

numeros = []

for i in range(cantidad):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)

buscar = int(input("Número a buscar: "))

encontrado = False

for i in range(cantidad):
    if numeros[i] == buscar:
        print("El número", buscar, "se encuentra en la posición", i)
        encontrado = True
        break

if encontrado == False:
    print("El número no se encuentra en la lista.")