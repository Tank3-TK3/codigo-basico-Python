print ("--------------------------------------------------")
calificaciones = {}
nummat = int(input("¿Cuantas materias tienes? "))
nummat = nummat - 1
numero2 = 0
while nummat >= numero2:
	a = input("Dame el nombre de la materia: ")
	b = float(input("Dame la calificacion: "))
	calificaciones [a] = b
	numero2 = numero2 + 1
resultado = calificaciones.values()
resultado = list(resultado)
sumMaterias = 0.0
for numero in resultado:
	 sumMaterias += float(numero)
prom = sumMaterias / len(resultado)
print ("Tu promedio es: ", prom)
print ("--------------------------------------------------")
max1 = max(calificaciones.values())
cal2 = list(calificaciones.items())
numero = False
a = 0
while numero == False:
	if max1 in cal2[a]:
		numero = True
	else:
		a = a + 1
print ("Tu materia con mejor promedio es: ", cal2[a])
print ("--------------------------------------------------")