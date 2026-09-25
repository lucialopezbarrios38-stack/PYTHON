suma = 0
suma_total = 0

for i in range (5):
    numeros = int(input("ingrese el numero:"))

    if numeros > 0:
        suma = suma + 1 
        suma_total = suma_total + numeros

print("suma", suma)
print("suma_total", suma_total)