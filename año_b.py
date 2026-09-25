anio=int(input("año:"))

if anio%4==0:
    if anio % 100==0:
        if anio % 400 == 0:
          print(f"el año {anio}es bisiesto.")
else:
    print(f"el año{anio}no es bisiesto.")


