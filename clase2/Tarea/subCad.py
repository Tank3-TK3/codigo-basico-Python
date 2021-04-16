b = "Esta es una subcadena de caracteres"
a = "Esta es una cadena de caracteres"
print (b.find("cara"))
print (a.find("cara"))
subcad = a[:10] in b
print (subcad)
subcad = b[15:] in a
print (subcad)