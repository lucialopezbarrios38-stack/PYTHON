cantidad = int(input("Cantidad: "))

positivos = 0
negativos = 0
ceros = 0

for i in range(cantidad):
    numero = int(input("Ingrese un número: "))

    if numero > 0:
        positivos = positivos + 1
    elif numero < 0:
        negativos = negativos + 1
    else:
        ceros = ceros + 1

print("Positivos:", positivos)
print("Negativos:", negativos)
print("Ceros:", ceros)