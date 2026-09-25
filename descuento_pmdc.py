valor_compra=float(input("valor de la compra:"))
if valor_compra>500000:
    descuento=valor_compra*0.10
else:
    descuento=0
    total_pagar=valor_compra-descuento

    print(f"descuento: ${descuento:,.0f}")
    print(f"total a pagar:${total_pagar:,.0f}")
