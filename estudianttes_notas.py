estudiantes = []
notas = []

cantidad= int(input("dime cuantos estudiantes aprovaron:"))

for i in range(cantidad):
    estudiante = input("Nombre:")
    nota = float(input("nota:"))

    estudiantes.append (estudiante)
    notas.append (nota)
    

print ("lista de estudiantes:")
for i in range (cantidad):
   print(estudiantes[i], "-" ,notas[i])


buscar = input("ingrese el estudiante:")
encontrado = "no encontrado"

for i in range (len(estudiantes)):
    if buscar == estudiantes [i]:
        encontrado=f"{buscar} esta en la posicion [i]y saco {notas[i]} de nota"
        break


print(encontrado)

suma = 0

for i in range (len(notas)):
    estudiantes = input("ingrese el estudiante")  
    nota =float(input("ingrese la nota"))  
    
    estudiantes.append(estudiante)
    notas.append (nota)

    suma += nota
    promedio = suma/cantidad

    
print("el promedio de las notas es: (promedio)")





    

