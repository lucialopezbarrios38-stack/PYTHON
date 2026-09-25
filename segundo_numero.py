cantidad = int(input("Cantidad de números: "))

numeros = []

for i in range(cantidad):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)

mayor = numeros[0]
segundo_mayor = numeros[0]

for numero in numeros:
    if numero > mayor:
        segundo_mayor = mayor
        mayor = numero
    elif numero > segundo_mayor and numero != mayor:
        segundo_mayor = numero

print("El segundo número mayor es:", segundo_mayor)