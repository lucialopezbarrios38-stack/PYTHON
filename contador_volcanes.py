palabra = input("Palabra: ")

contador = 0

for letra in palabra:
    if letra.lower() in "aeiou":
        contador = contador + 1

print("La palabra contiene", contador, "vocales.")