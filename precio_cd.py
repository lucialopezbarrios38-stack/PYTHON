precio_original= float(input("precio:"))
porcentaje_descuento= float(input("descuento:"))

valor_descuento= precio_original*(porcentaje_descuento / 100)
precio_final=precio_original- valor_descuento

print(f"precio original: ${precio_original:,.0f}". replace(",","."))
print(f"descuento aplicado: ${valor_descuento:,.0f}".replace(",","."))
print(f"precio final: ${precio_final:,.0f}".replace(",","."))