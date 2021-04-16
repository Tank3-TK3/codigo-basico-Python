def persona(añocur):
	nombres = []
	añosnac = []
	añoscumpl = []
	n = 0
	while n <= 2:
		nombres.append (input ("Dame un nombre: "))
		añosnac.append (int(input ("Dame su año de nacimiento: ")))
		añoscumpl.append (añocur - añosnac[n])
		n += 1
	n = 0
	while n <= 2:
		print (nombres[n],"tendras o tienes",añoscumpl[n],"años.")
		n += 1
añocur = int(input("Dame el año en curso: "))
persona(añocur)