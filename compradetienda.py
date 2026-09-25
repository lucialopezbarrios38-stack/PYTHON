compra = float(input("ingrese el valor de la compra:"))

descuento = compra * 0.20

if compra >= 100000:
    print ("se aplica el descuento del 20%")

elif 50000 <= compra < 99999:
    descuento = compra * 0.10
    print ("se aplica el descuento del 10%")
else:
  print("no hay descuento")

total = compra - descuento

print("dinero descontado:", descuento)
print("total a pagar:", total)
    
