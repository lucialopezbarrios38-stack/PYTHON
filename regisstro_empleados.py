cantidad = int(input("Cantidad de empleados: "))

empleados = {}

for i in range(cantidad):
    identificacion = input("Identificación: ")
    salario = float(input("Salario: "))

    empleados[identificacion] = salario

suma = 0

for salario in empleados.values():
    suma = suma + salario

promedio = suma / cantidad

print("Salario promedio: $", format(promedio, ".2f"))