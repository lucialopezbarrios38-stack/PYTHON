numero = int(input("Número: "))

suma = 0

for i in range(1, numero + 1):
    if i % 2 != 0:
        suma = suma + i

print("La suma de los números impares es:", suma)