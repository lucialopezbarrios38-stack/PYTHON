pares = 0
impares = 0

for i in range (10):
    numero= int( input("ingrese el numero:"))

    if numero % 2 == 0:
     print(" el numero es par")
     pares = pares + 1
else:
   print("el numero es impar")
   impares = impares + 1

   print("pares", pares)
   print("impares", impares)


