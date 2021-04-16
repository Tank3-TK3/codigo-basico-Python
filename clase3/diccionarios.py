print("--------------------------------------------------")
diccionario = {"total":55, "descuento":True, "recargos":"no aplica"}
print (diccionario)
diccionario["total"]=100
print (diccionario)
valor = diccionario["descuento"]
print (valor)
print("--------------------------------------------------")
diccionario2 = {"a":5, "b":2, "c":3}
print (diccionario2)
print("--------------------------------------------------")
resultado = "z" in diccionario2
print (resultado)
print("--------------------------------------------------")
print(diccionario2.get("a"))
print(diccionario2.get("z", "La llave z no existe"))
print("--------------------------------------------------")
resultado = diccionario2.setdefault("a", [])
print (resultado)
print("--------------------------------------------------")
diccionario3 = {"a":1, "b":2, "c":3, "d":4, "e":5}
resultado = diccionario3.keys()
resultado = tuple(resultado)
print (resultado)
resultado = list(resultado)
print (resultado)
resultado = diccionario3.values()
print (resultado)
resultado = list(resultado)
print (resultado)
resultado = diccionario3.items()
print (resultado)
resultado = list(resultado)
print (resultado)
print (len(diccionario3))
del diccionario3["a"]
diccionario3.pop("b")
print (len(diccionario3))
diccionario3.clear()
print (len(diccionario3))
print("--------------------------------------------------")
color_luz = "morado"
if color_luz == "verde":
	print ("Puede continuar")
elif color_luz == "amarillo":
	print ("Alto parcial")
elif color_luz == "rojo":
	print ("Alto total")
else:
	print ("Color no encontrado")
print("--------------------------------------------------")
print("--------------------------------------------------")
numero = 123456789
contador = 0

while numero >= 1:
	contador += 1
	numero = numero / 10
print ("La cantidad de digitos es: ", contador)
print("--------------------------------------------------")
print("--------------------------------------------------")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
 	print (numero)
 diccionario4 = {"a":1,"b":2}
 for elemento in diccionario4:
 	print (elemento)
print("--------------------------------------------------")
print("--------------------------------------------------")
valores = ((10, 20), ["text1", "text2"], (True, False))
for val1, val2 in valores:
	print (val1, val2)
for val1 in valores:
	print (val1)
print("--------------------------------------------------")
print("--------------------------------------------------")
for i in range(10):
	print (i)
print("--------------------------------------------------")
for i in range(2, 10):
	print (i)
print("--------------------------------------------------")
for i in range(-1, 20):
	print (i)
print("--------------------------------------------------")
for i in range(0, 101, 2):
	print (i)
print("--------------------------------------------------")
print("--------------------------------------------------")
lista = [1,2,3,4,5,6,7,8,9]
for i in range(len(lista)):
	print("indice: ", i, "valor :", lista[i])
print("--------------------------------------------------")
lista = [1,2,3,4,5,6,7,8,9]
for indice, valor in enumerate(lista):
	print("indice: ", indice, "valor :", valor)
print("--------------------------------------------------")
lista = [1,2,3,4,5,6,7,8,9]
for indice, valor in enumerate(lista, 2):
	print("indice: ", indice, "valor :", valor)
print("--------------------------------------------------")
print("--------------------------------------------------")
texto = "Crurso de Python Basico"
for caracter in texto:
	if caracter == "P":
		break
	print (caracter)
print("--------------------------------------------------")
texto = "Crurso de Python Basico"
for caracter in texto:
	if caracter == "P":
		continue
	print (caracter)
print("--------------------------------------------------")
print("--------------------------------------------------")
calificacion = int(input("Ingresa una calificacion: "))
if calificacion >= 8:
	print ("Aprobo")
else:
	print ("Reprobo")
print("--------------------------------------------------")
resultado = "Aprobo" if calificacion >=8 else "Reprobo"
print (resultado)
print("--------------------------------------------------")