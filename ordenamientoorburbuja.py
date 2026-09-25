numeros= [7,3,1,2,4,6,9,5,8]
for num in range(len(numeros)):
    for num in range (len(numeros)-1)#el menos 1 es para llegar a la ultima posicion

        if numeros[num] > numeros [num + 1]:
            numeros[num], numeros [num + 1] = numeros [num + 1], numeros[num]

print ("numeros ordenados:", numeros)

#odenamiento burbuja


