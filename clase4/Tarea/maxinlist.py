def max_in_list(lista):
	mayor = max(lista)
	print ("Tu numero mayor es: ", mayor)
lista = []
num = 1
fin = int (input ("Dame la cantidad de numeros a introducir: "))
while num <= fin:
	lista.append (float (input ("Dame un valor para la lista: ")))
	num += 1
print ("Tu lista de numeros es: ", lista)
max_in_list(lista)