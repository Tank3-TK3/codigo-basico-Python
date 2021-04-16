import os
import sys
import random

def numero_aleatorio(numnum):
	if numnum == 2:
		numnum = random.randint(10,99)
		adivina(numnum)
	elif numnum == 3:
		numnum = random.randint(100,999)
		adivina(numnum)
	elif numnum == 4:
		numnum = random.randint(1000,9999)
		adivina(numnum)
	elif numnum == 5:
		numnum = random.randint(10000,99999)
		adivina(numnum)
	elif numnum == 6:
		numnum = random.randint(100000,999999)
		adivina(numnum)
	elif numnum == 7:
		numnum = random.randint(1000000,9999999)
		adivina(numnum)
	elif numnum == 8:
		numnum = random.randint(10000000,99999999)
		adivina(numnum)
	elif numnum == 9:
		numnum = random.randint(100000000,999999999)
		adivina(numnum)
	else:
		os.system('cls')
		print ("Numero no dentro de el rango.")
		sys.exit()

def adivina(numnum):
	numnum = str(numnum)
	numnum2 = input("Intenta adivinar la cadena: ")
	if len(numnum2) == len(numnum):
		while numnum2 == numnum:
			if numnum2[0] == numnum[0]:
				pass
	else:
		print ("Cadena no valida")
		sys.exit()

numnum = int(input("Dime la longitud de la cadena (de 2 a 9): "))
numero_aleatorio(numnum)