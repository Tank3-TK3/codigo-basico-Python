def es_bisiesto(año):
	a = año%4  
	b = año%100 
	c = año%400 
	if (a == 0) and (b == c):
		print ("El año ", año ,"es bisiesto.")
	else:
		print ("El año ", año ,"no es bisiesto.")
año = float(input("Dame el año: "))
es_bisiesto(año)