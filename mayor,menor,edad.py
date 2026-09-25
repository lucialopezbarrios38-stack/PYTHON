edad = int(input("ingrese la edad:"))

if edad < 13:
    print("eres un niño")
if edad >= 13 and edad <= 17:
    print("eres un adolencente")
elif edad >=18 and edad <=59:
    print("eres un adulto")
else:
    print("eres un adulto mayor")

