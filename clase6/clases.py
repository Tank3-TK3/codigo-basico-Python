class Animals:
	def comer(self):
		print("Comiendo")
	def dormir(self):
		print("Durmiendo")

class Perro:
	def __init__(self, nombre):
		self.nombre = nombre
	def comer(self):
		print("Comiendo")
	def dormir(self):
		print("Durmiendo")
	def ladrar(self):
		print("Ladrando")
print("--------------------------------------------------")
firulais = Perro("Firulais")
firulais.comer()
firulais.dormir()
firulais.ladrar()
print("--------------------------------------------------")