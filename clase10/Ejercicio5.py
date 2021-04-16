#Escribir una función que simule el siguiente experimento: Se tiene una
#rata en una jaula con 3 caminos, entre los cuales elige al azar (cada uno tiene la
#misma probabilidad), si elige el 1 luego de 3 minutos vuelve a la jaula, si elige el 2
#luego de 5 minutos vuelve a la jaula, en el caso de elegir el 3 luego de 7 minutos
#sale de la jaula. La rata no aprende, siempre elige entre los 3 caminos con la misma
#probabilidad, pero quiere su libertad, por lo que recorrerá los caminos hasta salir de
#la jaula.
#La función debe devolver el tiempo que tarda la rata en salir de la jaula.
from random import randint
def laberinto (tiempo):
	camino = randint(1, 3)
	if (camino == 1):
		tiempo = laberinto(tiempo+3)
	elif (camino == 2):
		tiempo=laberinto(tiempo+5)
	else:
		tiempo += 7
	return tiempo

print(laberinto(0), "min")