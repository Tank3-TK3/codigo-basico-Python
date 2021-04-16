tupla1 = (1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 0)

elemento = tupla1 [4]
print (elemento)

subtupla = tupla1 [:9:2]
print (subtupla)

tupla2 = (1 , 2 , 3 , 4 , 5 , 6)

#uno, dos, tres, cuatro = tupla2 [0], tupla2 [1], tupla2 [2], tupla2 [3]
#uno, dos, tres, cuatro = tupla2
#uno, dos, tres, *cuatro = tupla2
uno, *dos, cinco, seis = tupla2

print (tupla2)
print (uno)
print (dos)
#print (tres)
#print (cuatro)
#print (uno, dos, tres, cuatro)
print (cinco)
print (seis)

tupla3 = (1, 2, 3, 4, 5, 6)
lista1 = [10, 20, 30, 40]
tupla4 = (100, 200, 300, 400)

resultado = zip(tupla3, lista1, tupla4)
#resultado = tuple(resultado)
resultado = list(resultado)
print (resultado)

lista2 = ["Python", "Java", "C","C++"]
tupla5 = ("Introduccion", "tuplas", "listas")

lista3 = list(tupla5)
print (lista5)
tupla6 = tuple(lista2)
print (tupla6)

mensaje = "Este es el taller de Python Basico"

tupla7 = tuple(mensaje)
lista4 = list(mensaje)

print (tupla7)
print (lista4)