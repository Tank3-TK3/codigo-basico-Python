"""
print("--------------------------------------------------")
class Usuario():
	def saludar(self, nombre):
		return "Hola: "+ nombre
jose = Usuario()
pepe = Usuario()

resultado = jose.saludar("Jose Perez")
resultado2 = jose.saludar("Jose Sanchez")
print (resultado)
print (resultado2)
print("--------------------------------------------------")
class Usuario():
	def saludar(self, nombre):
		return "Hola: "+ nombre
	def crear_nombre(self, nombre):
		self.nombre = nombre
	def mostrar_nombre(self):
		print (self.nombre)

jose = Usuario()
pepe = Usuario()

jose.crear_nombre("Jose Sanchez")
jose.mostrar_nombre()
print("--------------------------------------------------")
class Usuario():
	def __init__(self, username='', correo='', nombre=''):
		self.username = username
		self.correo = correo
		self.nombre = nombre

	def saludar(self):
		return "Hola: "+ self.nombre

jose = Usuario("JS", "@gmail.com", "Jose Sanches")
pepe = Usuario()

resultado = jose.saludar()
print (resultado)
print("--------------------------------------------------")
class Circulo:
	pi = 3.14159265 # variable de mi clase
	def __init__(self, radio):
		self.radio = radio #variable de tipo instancia

circulo_a = Circulo(10)
circulo_b = Circulo(20)

print (circulo_a.radio)
print (circulo_b.radio)

print (circulo_a.pi)
print (circulo_b.pi)

print (Circulo.pi)
"""
print("--------------------------------------------------")
class Triangulo:
	numero = 2
	@staticmethod
	def area(base,altura):
		return (base * altura)/Triangulo.numero

resultado = Triangulo.area(10, 20)
print (resultado)

print("--------------------------------------------------")
class Circulo:
	pi = 3.14159265
	@classmethod
	def area(cls, radio):
		return cls.pi * radio**2
c = Circulo()
print(c.area(10))
resultado = Circulo.area(5)
print (resultado)
print("--------------------------------------------------")