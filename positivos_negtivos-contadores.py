positivos = 0
negativos = 0
suma_positivos = 0

for i in range(10):
    numeros = int(input("ingrese el numero:"))

    if numeros > 0:
        print("es positivo")
        positivos = positivos + 1
        suma_positivos = suma_positivos + numeros

    elif numeros < 0:
      print("es negativo")
    negativos = negativos + 1

else:
   print(" es cero")
         

print("positivos", positivos)
print("negativos", negativos)
print("suma_positivos", suma_positivos)