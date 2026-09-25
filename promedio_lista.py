cantidad = int(input("Cantidad de calificaciones: "))

calificaciones = []

for i in range(cantidad):
    nota = float(input("Ingrese una calificación: "))
    calificaciones.append(nota)

suma = 0

for nota in calificaciones:
    suma = suma + nota

promedio = suma / cantidad

print("Promedio:", format(promedio, ".2f"))