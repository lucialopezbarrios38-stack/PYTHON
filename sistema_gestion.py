cantidad = int(input("Cantidad de estudiantes: "))

estudiantes = {}

for i in range(cantidad):
    codigo = input("Código: ")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    carrera = input("Carrera: ")
    promedio = float(input("Promedio: "))

    estudiantes[codigo] = {
        "nombre": nombre,
        "edad": edad,
        "carrera": carrera,
        "promedio": promedio
    }

mejor_codigo = ""
mejor_promedio = 0

for codigo, datos in estudiantes.items():
    if datos["promedio"] > mejor_promedio:
        mejor_promedio = datos["promedio"]
        mejor_codigo = codigo

print("Mejor estudiante")
print("Código:", mejor_codigo)
print("Nombre:", estudiantes[mejor_codigo]["nombre"])
print("Edad:", estudiantes[mejor_codigo]["edad"])
print("Carrera:", estudiantes[mejor_codigo]["carrera"])
print("Promedio:", estudiantes[mejor_codigo]["promedio"])