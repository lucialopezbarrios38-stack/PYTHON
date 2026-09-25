nombre=input("nombre:")
horas=int(input("horas trabajadas:"))
valor_hora=int(input("valor hora:"))

if horas <= 40:
    salario_bruto= horas * valor_hora
else:
    horas_extra = horas - 40
    salario_bruto = (40 * valor_hora) + (horas_extra * valor_hora * 1.5)

if salario_bruto > 5000000:
   descuento: float= salario_bruto * 0.12
elif salario_bruto > 3000000:
 descuento: float=salario_bruto * 0.08
else:
 descuento= 0

salario_neto= salario_bruto-descuento


print("empleado:", nombre)
print("salario bruto: $", int(salario_bruto))
print("descuento: $", int(descuento))
print("salario neto: $", int(salario_neto))   
 
    