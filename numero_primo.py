numero = int(input("Número: "))

primo = True

if numero < 2:
    primo = False
else:
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break

if primo:
    print("El número", numero, "es primo.")
else:
    print("El número", numero, "no es primo.")