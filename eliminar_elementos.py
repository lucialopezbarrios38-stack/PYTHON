cantidad = int(input("Cantidad de números: "))

numeros = []
sin_repetir = []

for i in range(cantidad):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)

for numero in numeros:
    if numero not in sin_repetir:
        sin_repetir.append(numero)

print("Lista sin elementos repetidos:")

for numero in sin_repetir:
    print(numero)