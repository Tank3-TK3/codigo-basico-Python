def frecuencias(secuencias):
	frec = dict()
	for elementos in secuencias:
		frec[elementos] = frec.get(elementos, 0) + 1
	print(frec)
print ("--------------------------------------------------")
frecuencias(["peras","manzanas","peras"])
frecuencias((1,2,3,4,3,2,1))
#frecuencias(1) no se puede!!!
print ("--------------------------------------------------")