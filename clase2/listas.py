lenguajes = ["Python","C","C++","C#","Django","R","Java"]

#[:] todos los elemntos de la lista.
#[start:] todos los elementos desde el indice establesido.
#[:end] todos los elementos desde el indice 0 hasta el establesiodo.
#[start:end] todos los elemenos dentro de un rango establesido.
#[start:end:step] todos los elementos dentro de un rango con saltos.


resultados1 = lenguajes[2]
resultados2 = lenguajes[-1]
resultados3 = lenguajes[-3]
resultados4 = lenguajes[0:3]
resultados5 = lenguajes[:4]
resultados6 = lenguajes[2:]
resultados7 = lenguajes[0:9]
resultados8 = lenguajes[:]
resultados9 = lenguajes[1:7:2]
resultados10 = lenguajes[::-1]

print (resultados1)
print (resultados2)
print (resultados3)
print (resultados4)
print (resultados5)
print (resultados6)
print (resultados7)
print (resultados8)
print (resultados9)
print (resultados10)


numeros = [8.17 , 90 , 1 , 5 , 5 , 44 , 1.32]

numeros.sort() #Ordena la lista en orden asendente
print (numeros)

numeros.sort(reverse = True) #Ordena la lista en orden decendente
print (numeros)


menor = min(numeros) #numero menor
mayor = max(numeros) #numero mayor
longitud = len(numeros) #longitud de la lista
resultado = 8 in numeros
index = numeros.index(8.17)
contador = numeros.count(5)

print (menor)
print (mayor)
print (longitud)
print (resultado)
print (index)
print (contador)


fila_uno = [10 , 20 , 50]
fila_dos = [30 , 40 , 40]

matriz = [fila_uno,fila_dos]
print (matriz)

primer_elemento = matriz [0][2]
print (primer_elemento)
