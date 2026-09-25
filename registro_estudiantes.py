cantidad = int(input("Cantidad de estudiantes: "))

estudiantes = {}

for i in range(cantidad):
    codigo = input("Código: ")
    nombre = input("Nombre: ")

    estudiantes[codigo] = nombre

print("Listado de estudiantes")

for codigo, nombre in estudiantes.items():
    print(codigo, "->", nombre)