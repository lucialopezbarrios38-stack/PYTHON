estudiantes = []
notas = []

while True:
    print("===== MENÚ =====")
    print("1. Registrar estudiantes")
    print("2. Buscar estudiante")
    print("3. Mostrar promedio")
    print("4. Mostrar todos")
    print("5. Mostrar aprobados y desaprobados")
    print("6. Salir")

    opcion = int(input("Seleccione una opción: "))

    match opcion:

        case 1:
            cantidad = int(input("Cantidad de estudiantes: "))

            for i in range(cantidad):
                nombre = input("Nombre: ")
                nota = float(input("Nota: "))

                estudiantes.append(nombre)
                notas.append(nota)

        case 2:
            buscar = input("Ingrese el nombre: ")
            encontrado = False

            for i in range(len(estudiantes)):
                if estudiantes[i] == buscar:
                    print("Posición:", i + 1)
                    print("El estudiante", estudiantes[i], "sacó", notas[i])
                    encontrado = True

            if encontrado == False:
                print("Estudiante no encontrado")

        case 3:
            if len(notas) > 0:
                suma = 0

                for i in range(len(notas)):
                    suma += notas[i]

                promedio = suma / len(notas)

                print("El promedio es:", promedio)

            else:
                print("No hay estudiantes registrados")

        case 4:
            if len(estudiantes) > 0:

                for i in range(len(estudiantes)):
                    print(i + 1, estudiantes[i], "-", notas[i])

            else:
                print("No hay estudiantes registrados")

        case 5:
            if len(estudiantes) > 0:

                aprobados = 0
                desaprobados = 0

                for i in range(len(estudiantes)):

                    if notas[i] >= 3.0:
                        print(estudiantes[i], "-", notas[i], "- APROBADO")
                        aprobados += 1

                    else:
                        print(estudiantes[i], "-", notas[i], "- DESAPROBADO")
                        desaprobados += 1

                print("Total de aprobados:", aprobados)
                print("Total de desaprobados:", desaprobados)

            else:
                print("No hay estudiantes registrados")

        case 6:
            print("Programa finalizado")
            break

        case _:
            print("Opción inválida")