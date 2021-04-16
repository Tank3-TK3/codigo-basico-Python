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