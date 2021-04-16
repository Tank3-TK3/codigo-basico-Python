def filtrar_palabra(lista, fin, n):
	num = 0
	while num <= (fin-1):
		if len(lista[num]) <= n :
			lista.pop(num)
			num = 0
			fin -= 1
			print (lista)
		else:
			num += 1
	print("Tus palabras con", n ,"letras o mas, son:", lista)
lista = []
num = 1
fin = int (input ("Dame la cantidad de palabras a filtrar: "))
while num <= fin:
	lista.append (input ("Dame una palabra para la lista: "))
	num += 1
n = int (input ("Dame el numero minimo de letras para la palabra: "))
filtrar_palabra(lista, fin, n)