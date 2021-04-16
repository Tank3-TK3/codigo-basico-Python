"""
class Animal:
	def comer(self):
		print("Comiendo")
	def dormir(self):
		print("Durmiendo")
	#def comun(self):
		#print("Metodo comun para Animal")

class Mascota:
	def fecha_adopcion(self,fecha):
		self.fecha_adopcion = fecha
	#def comun(self):
		#print("Metodo comun para Mascota")

class Perro(Animal,Mascota):
	def __init__(self, nombre):
		self.nombre = nombre
	def ladrar(self):
		print("Ladrando")
	def dormir(self):
		print(self.nombre," esta durmiendo.")
		Animal.dormir(self)
		print("No molestar")
	#def comun(self):
		#print("Metodo comun para Perro")
"""
"""
class Gato(Animal,Mascota):
	def __init__(self,nombre):
		self.nombre = nombre
	def ronronear(self):
		print("Ronroneando")
"""
"""
print("--------------------------------------------------")
firulais = Perro("Firulais")
firulais.comer()
firulais.dormir()
firulais.ladrar()
firulais.fecha_adopcion("Hoy")
print(firulais.fecha_adopcion)
#firulais.comun()
print("--------------------------------------------------")
"""
"""
garfield = Gato("Garfield")
garfield.comer()
garfield.dormir()
garfield.ronronear()
garfield.fecha_adopcion("Ayer")
print(garfield.fecha_adopcion)
print("--------------------------------------------------")
"""
class Gato:
	def __init__(self,nombre):
		self.nombre = nombre
	def __str__(self):
		return self.nombre

class Pato(object):
	def __init__(self,nombre):
		self.nombre = nombre
	def __str__(self):
		return self.nombre
print("--------------------------------------------------")
gato = Gato("Garfield")
gato.edad = 6
pato = Pato("Lucas")
print(gato.__dict__)
print(pato.__dict__)
print("--------------------------------------------------")