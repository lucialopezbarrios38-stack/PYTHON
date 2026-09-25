def cajero_automatico():
    saldo = 1000  # Saldo inicial del usuario
    while True:
        print("Bienvenido al cajero automático")
        print("Seleccione una opción:")
        print("1. Consultar saldo")
        print("2. Retirar dinero")
        print("3. Depositar dinero")
        print("4. Salir")

    opcion = input("Ingrese el número de la opción: ")

    if opcion == "1":
       print(f"su saldo actual es: ${saldo:.2f}")
    elif opcion == "2":
        cantidad = float(input("Ingrese la cantidad a depositar: "))
        if cantidad <= 0:
            saldo += cantidad
            print(f"deposito exitoso. Su nuevo saldo es: ${saldo:.2f}")
        else:
            print("cantidad invalida.")
    elif opcion == "3":
        cantidad = float(input("Ingrese la cantidad a retirar: "))
        if cantidad > 0 and cantidad <= saldo:
            saldo -= cantidad
            print(f"Retiro exitoso. Su nuevo saldo es: ${saldo:.2f}")
        else:
            print("fondos insuficientes o cantidad invalidad.")
    elif opcion == "4":
        print("saliendo del sistema, ¡Hasta luego!")
           
    else:
        print("Opción inválida. Por favor, intente nuevamente.")
    

if __name__ == "__main__":
        cajero_automatico()
