class Multimedia:
	def __init__(self,titulo,autor,formato,duracion):
		self.titulo = titulo
		self.autor = autor
		self.formato = formato
		self.duracion = duracion
	def __str__(self):
		return """Titulo:\t\t{}\nAutor:\t\t{}\nFormato:\t{}\nDuracion:\t{}
		""".format(self.titulo,self.autor,self.formato,self.duracion)
	def compara(self):
		if (self.titulo==self.autor):
			return True
		else:
			return False

class Pelicula(Multimedia):
	def __init__(self,titulo,autor,formato,duracion,actor_principal,actriz_principal):
		self.titulo = titulo
		self.autor = autor
		self.formato = formato
		self.duracion = duracion
		self.actor_principal = actor_principal
		self.actriz_principal = actriz_principal
	def __str__(self):
		return """Titulo:\t\t\t{}\nAutor:\t\t\t{}\nFormato:\t\t{}\nDuracion:\t\t{}\nActor Principal:\t{}\nActriz Principal:\t{}
		""".format(self.titulo,self.autor,self.formato,self.duracion,self.actor_principal,self.actriz_principal)

class ListaMultimedia():
	archivos = []
	contar = 0
	def  __init__(self,archivos=[]):
		self.archivos = archivos
	def agregar(self,p):
		self.archivos.append(p)
		self.contar += 1
	def mostrar(self):
		for p in self.archivos:
			print(p)
	def cantidad(self):
		return"""Total de objetos en la lista: {}""".format(self.contar)

print("--------------------------------------------------")
c = ListaMultimedia()
c.mostrar()
c.agregar(Pelicula("Rob","Rob","dvd","2:30:00","Abn","Lil"))
c.agregar(Multimedia("SaS","Bob","mp3","03:00",))
c.mostrar()
print(c.cantidad())
print("--------------------------------------------------")