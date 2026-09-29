

x1 = int(input("Posición del canguro 1: "))
v1 = int(input("Salto del canguro 1: "))
x2 = int(input("Posición del canguro 2: "))
v2 = int(input("Salto del canguro 2: "))

if v1 <= v2:
    print("NO")
else:
    if (x2 - x1) % (v1 - v2) == 0:
        print("YES")
    else:
        print("NO")



