print ("--------------------------------------------------")
def saludar():
	print ("Hola mundo")
saludar()
print ("--------------------------------------------------")
def crear_mensaje(nombre):
	mensaje = "Hola {}, bienvenido a las funciones".format(nombre)
	return mensaje
nuevo_mensaje = crear_mensaje("Roberto")
print (nuevo_mensaje)
print ("--------------------------------------------------")
def suma(val1, val2, val3):
	return val1 + val2 + val3
resultado = suma(10, 20, 30)
print(resultado)
print ("--------------------------------------------------")
def obtener_curso():
	return "Cruso de Python", "Basico", "3.6"
nombre, nivel, version = obtener_curso()
print (nombre, nivel, version)
print ("--------------------------------------------------")
def crear_usuario(nombre, apellido, edad=10):
	return {
		'nombre': nombre,
		'apellido': apellido,
		'edad': edad,
		'nombre_completo': "{} {}".format(nombre, apellido)
	}
usuario = crear_usuario("Roberto", "Cruz Lozano", 21)
print (usuario["nombre"])
print (usuario["apellido"])
print (usuario["edad"])
print (usuario["nombre_completo"])
print ("--------------------------------------------------")
def suma2(prametro_requerido, *args):
	total = 0
	print (prametro_requerido)
	for valor in args:
		total = total + valor
	return total
resultado2 = suma2("Argumento requerido", 10, 20, 30, 40, 50)
print(resultado2)
print ("--------------------------------------------------")
def usuarios_autenticados(**kwargs):
	print (kwargs)
usuarios_autenticados(nombre="Roberto", años="21")
print ("--------------------------------------------------")
def combinacion(requerido, *args, **kwargs):
	print (requerido)
	print (args)
	print (kwargs)
combinacion("Argumento requerido", 10, 20, v=True, f=False)
print ("--------------------------------------------------")
def mi_funcion():
	print ("mensaje1")
	return "<-aqui termina la funcion"
	print ("mensaje2")
resultado = mi_funcion()
print (resultado)
print ("--------------------------------------------------")
animal = "Leon"
def mostrar_animal():
	global animal
	animal = "Perro"
	print(animal)
mostrar_animal()
print (animal)
print ("--------------------------------------------------")
def centigrados_farhenheit(grados):
	return grados * 1.8 + 32
funcion_variable = centigrados_farhenheit
resultado = funcion_variable(32)
print (resultado)

mi_funcion2 = lambda grados = 0: grados*1.8+32
resultado = mi_funcion2(32)
print (resultado)
print ("--------------------------------------------------")
def comenzar_play_list(lista):
	def reproducir():
		nonlocal lista
		lista = ["track4", "track5", "track6"]
		for val in lista:
			print (val)
	reproducir()
lista = ["track1", "track2", "track3"]
comenzar_play_list(lista)
print ("--------------------------------------------------")