palabra = input("Palabra: ")

contador = {}

for letra in palabra.lower():
    if letra in contador:
        contador[letra] = contador[letra] + 1
    else:
        contador[letra] = 1

for letra, cantidad in contador.items():
    print(letra, ":", cantidad)