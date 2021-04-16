"""
curso = "Curso de Python"

tam = len(curso) #tamaño del string
print (tam)

car = curso [2] #caracter en un indise establesido
print (car)

sub = curso [1:15:2] #crear subString
print (sub)

#curso [2] = "e" (no se puede)
"""
lenguajes1 = "Python Java C C++"
res1 = lenguajes1.split()
print (res1)

lenguajes2 = "Python;Java;C;C++"
res2 = lenguajes2.split(";")
print (res2)

nuevo_string = " ".join(res2)
print (nuevo_string)

texto1 = """Este es 
			uno de 
			varias lineas"""

res3 = texto1.splitlines()
print (res3)
"""
texto2 = "curso de Python Basico"

res4 = texto2.swapcase()
print (res4)

res5 = texto2.upper()
print (res5)

res6 = texto2.lower()
print (res6)

res7 = texto2.capitalize()
print (res7)

res8 = texto2.islower()
print (res8)

res9 = texto2.isupper()
print (res9)

res10 = texto2.title()
print (res10)

res11 = texto2.replace("Python", "Django")
print (res11)

res12 = texto2.strip()
print (res12)

curso = "Python"
horario = "Viernes de 9 a 13"

res13 = "Curso de %s %s" %(curso, horario)
print (res13)

res14 = "Curso de {a} {b}".format(a=curso, b=horario)
print (res14)

curso2 = "Curso de Python Basico"
#curso2 = "q" + curso2[1:] + " en la Facultad de Informatica"
curso2 = "q" + curso2[1:] + " con " + str(20) + " alumnos."
print (curso2)

mensaje = "Este es un mensaje en cuanto de varios caracteres"

res15 = mensaje.count("mensaje")
print (res15)

res16 = "mensaje" in mensaje
print (res16)

res17 = "mensaje" not in mensaje
print (res17)

res18 = mensaje.find("mensaje")
print (res18)

res19 = mensaje[res18 : res18+len("mensaje")]
print (res19)

res20 = mensaje.startswith("Este")
print (res20)

res21 = mensaje.endswith("caracteres")
print (res21)
"""