def mas_larga(lista):
	tam = []
	num = 1
	bandera1 = 0
	bandera2 = 0
	while num <= fin:
		tam.append(len(lista[num-1]))
		bandera1 = num-1
		if tam[bandera1] > tam[bandera2] :
			bandera2 = num-1
		num += 1
	print("Tu palabra mas larga es: ", lista[bandera2])
lista = []
num = 1
fin = int (input ("Dame la cantidad de palabras a introducir: "))
while num <= fin:
	lista.append (input ("Dame una palabra para la lista: "))
	num += 1
mas_larga(lista)