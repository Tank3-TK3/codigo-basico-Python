#Escribir una función recursiva que encuentre el mayor elemento de una lista.

def Mayor(lista, numero, mayor, bandera):
	if (lista[0] > lista[numero] and bandera == 0):
		mayor = lista[numero]
		bandera = bandera + 1
		return Mayor(lista, numero-1, mayor, bandera)
	else:
		if (numero == 0 and lista[numero] > mayor):
			print("El numero mayor de la lista es: ", lista[numero])
		elif (numero == 0):
			print("El numero mayor de la lista es: ", mayor)
		elif (lista[numero] > mayor):
			mayor = lista[numero]
			return Mayor(lista, numero-1, mayor, bandera)
		elif (mayor > lista[numero]):
			print("El numero mayor de la lista es: ", mayor)

lista = []
numero = int(input("Ingresa el numero de elementos de la lista: "))
q = 0.0
bandera = 0

for x in range(0,numero):
	q = float(input("Ingresa un numero a la lista: "))
	lista.append(q)

Mayor(lista, numero-1, lista[0], bandera)