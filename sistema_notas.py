cantidad = int(input("Cantidad de estudiantes: "))

estudiantes = {}

for i in range(cantidad):
    nombre = input("Nombre: ")
    nota = float(input("Nota: "))

    estudiantes[nombre] = nota

mejor_estudiante = ""
mejor_nota = 0

for nombre, nota in estudiantes.items():
    if nota > mejor_nota:
        mejor_nota = nota
        mejor_estudiante = nombre

print("El estudiante con la mejor nota es:")
print(mejor_estudiante, "->", mejor_nota)