
a = [2, 4]
b = [16, 32, 96]

contador = 0

for numero in range(1, 101):
    sirve = True

    for x in a:
        if numero % x != 0:
            sirve = False

    for x in b:
        if x % numero != 0:
            sirve = False

    if sirve:
        contador = contador + 1

print(contador)


