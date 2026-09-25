edad= int(input("edad:"))

if 0 <=edad<=12:
    print("clasificacion: niño")
elif 13<=edad<=17:
    print("clasificacion: adolecente")
elif 18<=edad <=59:
    print("clasificacion: adulto")
elif edad >=60:
    print("clasificacion: adulto mayor")

else:
    print("edad invalida")