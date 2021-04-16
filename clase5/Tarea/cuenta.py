class Cuenta():
	cuenta=0.0
	def __init__(self,titular=''):
		print ("Se creo una cuenta con titular: "+titular)
		self.titular = titular
	def ingresar(self,cuenta=''):
		if (float(cuenta) >= 0):
			self.cuenta = self.cuenta + float(cuenta)
			print ("Se ingreso a la cuenta "+self.titular+" la cantidad de: $"+cuenta)
		else:
			print ("No se ingreso nada a la cuenta.")
	def retirar(self,cuenta=''):
		self.cuenta = self.cuenta - float(cuenta)
		print ("Se retiro de la cuenta "+self.titular+" la cantidad de: $"+cuenta)
		if (self.cuenta < 0):
			self.cuenta=0
print("--------------------------------------------------")
cuenta = Cuenta(input("Dame el nombre del titular: "))
print("--------------------------------------------------")
cuenta.ingresar(input("Dame la cantida a ingresar: "))
cuenta.ingresar(input("Dame la cantida a ingresar: "))
print("--------------------------------------------------")
print("El total en la cuenta es: $"+str(cuenta.cuenta))
print("--------------------------------------------------")
cuenta.retirar(input("Dame la cantida a retirar: "))
cuenta.retirar(input("Dame la cantida a retirar: "))
print("--------------------------------------------------")
print("El total en la cuenta es: $"+str(cuenta.cuenta))
print("--------------------------------------------------")