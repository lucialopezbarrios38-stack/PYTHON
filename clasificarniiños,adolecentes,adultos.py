niños = 0
adolecentes = 0
adultos = 0

for i in range (10):
    edad = int(input("ingresa la edad:" ))

    if edad <= 13:
      niños = niños + 1

    elif edad <= 17:
       adolecentes = adolecentes + 1

    else:
       adultos = adultos + 1

print("niños", niños)
print("adolecentes", adolecentes)
print("adutos", adultos)
