print("--------------------------------------------------")
import os
fila_uno = []
fila_dos = []
fila_tres = []
fila_cuatro = []
fila_cinco = []
num = 0
while num <= 4:
	fila_uno.append (float (input ("Dame un valor para la fila uno: ")))
	num += 1
print("--------------------------------------------------")
num = 0
while num <= 4:
	fila_dos.append (float (input ("Dame un valor para la fila dos: ")))
	num += 1
print("--------------------------------------------------")
num = 0
while num <= 4:
	fila_tres.append (float (input ("Dame un valor para la fila tres: ")))
	num += 1
print("--------------------------------------------------")
num = 0
while num <= 4:
	fila_cuatro.append (float (input ("Dame un valor para la fila cuatro: ")))
	num += 1
print("--------------------------------------------------")
num = 0
while num <= 4:
	fila_cinco.append (float (input ("Dame un valor para la fila cinco: ")))
	num += 1
os.system('cls')
print("--------------------------------------------------")
matriz = [fila_uno,fila_dos,fila_tres,fila_cuatro,fila_cinco]
print (matriz)
print("--------------------------------------------------")
print ("El punto silla de la matriz es: ")
print("--------------------------------------------------")