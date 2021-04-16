print ("--------------------------------------------------")
import os
numeros = []
num = 0
while num <= 9:
	numeros.append (float (input ("Dame un valor: ")))
	num += 1
os.system('cls')
print ("--------------------------------------------------")
print (numeros)
suma = 0.0
for numero in numeros:
	 suma += numero
print ("La suma de todos tus numeros es: ", suma)
print ("El promedio de todos tus numeros es: ", suma / len(numeros))
print ("El numero mayor: ", max(numeros))
print ("El numero menor: ", min(numeros))
print ("--------------------------------------------------")