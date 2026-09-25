#programa en el cual el usuario ingrese una palabra y el mismo promagrama te diga cuantas vocales tiene
palabra= str(input("ingrese la palabra:"))
contador = 0

for letra in palabra:
 if letra in "aeiou":
  contador = contador + 1
print("la palabra tiene",contador, "vocales.")

