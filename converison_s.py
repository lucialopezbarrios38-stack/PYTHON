total_segundos=int(input("segundos: "))
horas = total_segundos// 3600
minutos=(total_segundos%3600)// 60
segundos_restantes= total_segundos%60

print(f"{total_segundos} segundos equivalen a:")
print(f"{horas} horas(s)")
print(f"{minutos} minutos(s)")
print(f"{segundos_restantes} segundos(s)")
