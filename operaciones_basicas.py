
def sumar (a,b):
    return a + b
def resta (a,b):
   return a-b
def multiplicar (a,b):
     return a * b
def dividir (a,b):
  if b==0:
   return "error:division por cero no permitida"
  return a/b

def calculadora():
  print("seleccione la operacion:")
  print("1. suma")
  print("2. resta")
  print("3. multiplicacion")
  print("4. division")

opcion= input("ingrese el numero de la operacion(1/2/3/4): ")
if opcion in ('1','2','3','4'):
     try:

        num1= float(input("ingrese el primer nuero:"))
        num2= float(input("ingrese el segundo numero:"))
     except ValueError:
       print("por favor ingrese valores numericos validos.")

if opcion== '1':
   print(f"resultado: {sumar(num1,num2)}")
elif opcion== '2':
   print(f"resultado: {resta(num1,num2)}")
elif opcion== '3':
   print(f"resultado: {multiplicar(num1,num2)}")
elif opcion== '4':
   print(f"resultado: {dividir(num1,num2)}")

else:
  print("opcion invalida")

if __name__ == "__main__":
    calculadora()




