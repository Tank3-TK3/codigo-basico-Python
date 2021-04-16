class SoyUnico(object):
	__instance = None
	nombre = None
	def __str__(self):
		return 'self ' + self.nombre
	def __new__(cls):
		if SoyUnico.__instance is None:
			SoyUnico.__instance = object.__new__(cls)
		return SoyUnico.__instance
print ("--------------------------------------------------")
personaUnica = SoyUnico()
personaUnica.nombre = "SoyUnico"
print(personaUnica)
print(id(personaUnica))
print ("--------------------------------------------------")
otraPersona = SoyUnico()
otraPersona.nombre = "Soy otra persona"
print(otraPersona)
print(id(otraPersona))
print ("--------------------------------------------------")
print(personaUnica)
print(otraPersona)
print ("--------------------------------------------------")