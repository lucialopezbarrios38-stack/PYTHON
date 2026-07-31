#calcular el precio total de una compra

precioproducto = float(input('ingrese el precio del producto:'))
iva = float(input('ingrese el porcentaje del IVA:'))

valorIva = precioproducto* iva/100
preciototal = precioproducto + valorIva

print()
print('resumen de la compra')
print("---------------------")
print("el precio del producto es:", precioproducto)
print("el valor del iva es:", preciototal)
print("el precio total que debe pagar es:", preciototal)
print("gracias por su compra, vuelva pronto")