print ("--------------------------------------------------")
import os
frases1, frases2, frases3, frases4 = [], [], [], []
fra1 = int (input ("¿Cuantas frases tienes? "))
print ("--------------------------------------------------")
num = 0
while num <= (fra1 - 1):
	frases1.append (input ("Dame una frase (posiblemente palindroma): "))
	frases1[num] = frases1[num].lower()
	frases2.append (frases1[num].replace(" ", ""))
	frases3.append (frases2[num][::-1])
	frases4.append (frases1[num])
	if frases2[num] in frases3[num]:
		frases4 [num] = "Es un palindromo: " + frases1[num]
	else:
		frases4 [num] = "No es un palindromo: " + frases1[num]
	num += 1
os.system('cls')
print ("--------------------------------------------------")
print (frases1)
print (frases4)
print ("--------------------------------------------------")