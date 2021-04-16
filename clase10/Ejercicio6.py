#Escribir una función que reciba 2 enteros n y b y devuelva True si n es potencia de b.

def Potencia(n,b):
	c = 1
	if (n == 1):
		print ("(Todo numero elevado a la 0 resulta 1)")
		return True
	else:
		if (b > n):
			return False
		else :
			if (n%b != 0):
				return False
			else :
				while c < n:
					c = c * b
				if c == n:
					return True
				else:
					return False

n = int(input("Ingresa un numero: "))
b = int(input("Ingresa el numero potencia: "))

print(Potencia(n,b))