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