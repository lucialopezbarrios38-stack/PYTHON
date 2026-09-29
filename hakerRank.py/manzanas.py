
s = int(input("Inicio de la casa: "))
t = int(input("Final de la casa: "))

a = int(input("Posición del manzano: "))
b = int(input("Posición del naranjo: "))

m = int(input("Cantidad de manzanas: "))
n = int(input("Cantidad de naranjas: "))

manzanas = list(map(int, input("Distancias de las manzanas: ").split()))
naranjas = list(map(int, input("Distancias de las naranjas: ").split()))

contador_manzanas = 0
contador_naranjas = 0

for x in manzanas:
    posicion = a + x

    if posicion >= s and posicion <= t:
        contador_manzanas = contador_manzanas + 1

for x in naranjas:
    posicion = b + x

    if posicion >= s and posicion <= t:
        contador_naranjas = contador_naranjas + 1

print(contador_manzanas)
print(contador_naranjas)
