print ("--------------------------------")
nombre_tutor = "Raquel"
CONSTANTE = "soy una constante"
print (nombre_tutor)
print (CONSTANTE)
print ("--------------------------------")
valor_uno, valor_dos, valor_tres = 10, "Raquel", 10*20
print (valor_uno, valor_dos, valor_tres)
#Este es un comentario de linea

"""
	Este es un 
	comentario 
	de varias 
	lineas
"""
print ("--------------------------------")
nombre = input("Ingresa tu nombre:")
print ("Bienvenido: ", nombre)
edad = int(input("Ingresa tu edad: "))
print ("En 10 años tendras: ", edad+10)
peso = float(input("Dame tu peso: "))
print ("Tu peso es: ", peso)
print ("--------------------------------")
valor_cuatro = 10
valor_cinco = 18

mayor = valor_cuatro > valor_cinco
print (mayor)
menor = valor_cuatro < valor_cinco
print (menor)
mayor_igual =  valor_cuatro >= valor_cinco
print (mayor_igual)
menor_igual = valor_cuatro <= valor_cinco
print (menor_igual)
igual = valor_cuatro == valor_cinco
#igual = valor_cuatro is valor_cinco
print (igual)
diferente = valor_cuatro != valor_cinco
print (diferente)
print ("--------------------------------")
print ("Estas autorisado? si/no")
autorizacion = input() == "si"
print (autorizacion)
print ("--------------------------------")