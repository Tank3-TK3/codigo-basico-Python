import math
print ("Para calcular la longitud de 1 vualtea de una llanta es:")
print ("longitud = 2 * pi * r")
print ("Si tenemos una llanta de 50 cm de dianmetro y recorre 1 km...")
longitud = 2 * math.pi * 0.25
print ("Entonces:")
print ("longitud = 2 * pi * 0.25 m")
print ("Lo que es igual a: ", longitud, "m de solo una vuelta.")
print ("Por lo tanto la llanta da un total de vueltas en:")
print ("vueltas = 1000 m /", longitud, "m")
vueltas = 1000 / longitud
print ("Lo que da como resultado: ", vueltas, "vueltas en 1km.")