personas = {
    "nombre": "Carlos",
    "edad": 20,
    "ciudad": "Bogotá"
}

while True:

    print("\n===== MENÚ =====")
    print("1. Mostrar información")
    print("2. Cambiar edad")
    print("3. Agregar profesión")
    print("4. Eliminar ciudad")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        print("\n--- INFORMACIÓN ---")
        print("Nombre:", personas["nombre"])
        print("Edad:", personas["edad"])
        print("Ciudad:", personas["ciudad"])

    elif opcion == 2:
        nueva_edad = int(input("Ingrese la nueva edad: "))
        personas["edad"] = nueva_edad
        print("Edad actualizada.")

    elif opcion == 3:
        profesion = input("Ingrese la profesión: ")
        personas["profesion"] = profesion
        print("Profesión agregada.")

    elif opcion == 4:
        del personas["ciudad"]
        print("Ciudad eliminada.")

    elif opcion == 5:
        print("Programa terminado.")
        break

    else:
        print("Opción no válida.")