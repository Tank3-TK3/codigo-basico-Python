def edad(numedades):
	edades = []
	edades20 = []
	n = 0
	while n <= (numedades-1):
		edades.append(int(input ("Dame una edad: ")))
		if edades[n] > 20:
			edades20.append(edades[n])
		n += 1
	edades = tuple(edades)
	print ("Tus edades: ", edades)
	print ("Las edades mayores a 20 años, son: ", edades20)
numedades = int(input("Dame el numero de edades: "))
edad(numedades)