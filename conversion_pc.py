pesos= float(input("pesos_colombianos:"))

tasa_usd= 4000
tasa_eur= 4600

dolares= pesos/tasa_usd
euros= pesos/ tasa_eur

print(f"pesos colombianos: ${pesos:,.0f}". replace(",","."))
print(f"dolares:${dolares:,.2f} USD")
print(f"euros:€{ euros:,.2f} EUR")

