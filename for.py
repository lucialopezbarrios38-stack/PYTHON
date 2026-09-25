positivos = 0
negativos = 0
ceros = 0

for numero in range (5):
    numero =int(input("ingrese el numero:"))
    

    if numero > 0:
     print("el numero es positivo")
     positivos = positivos + 1

    elif numero < 0:
     print("el numero es negativo")
     negativos= negativos + 1
    else:
      print("es igual a cero")
    ceros = ceros + 1

print("positivos", positivos)
print("negativos", negativos)
print("ceros", ceros)