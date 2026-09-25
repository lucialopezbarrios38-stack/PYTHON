registrar = int(input("dame el vehiculo: "))

vehiculo={}

for i in range(registrar):
    placa = input("placa: ")
    marca = input("marca: ")
    año = input("año:")

vehiculo[placa] = marca

buscar = input("vehiculo registrado: ")
if buscar in vehiculo:
    print("vehiculo registrado:")
    print(buscar, "->", vehiculo[buscar])
else:
    print(" registrado el vehiculo.")

mostrar = input("vehiculo mas antiguo: ")
if mostrar in vehiculo:
    print("vehiculo mas antiguo:")
    print(mostrar, "->", vehiculo[mostrar])
else:
    print("mostrar el vehiculo" )


