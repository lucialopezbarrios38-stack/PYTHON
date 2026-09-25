mayor_edad = 0
menor_edad = 0

for i in range(8):
    edad = int(input("ingrese la edad:"))

    if edad > 18:
        print("es mayor de edad")
        mayor_edad = mayor_edad + 1
    else: 
      print("es menor de edad")
      menor_edad = menor_edad + 1

print("mayor_edad", mayor_edad)
print("menor_edad", menor_edad)