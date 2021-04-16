from PIL import Image # El módulo proporciona una clase con el mismo 
					  # nombre que se utiliza para representar una 
					  # imagen PIL. El módulo también proporciona 
					  # una serie de funciones de fábrica, incluidas 
					  # funciones para cargar imágenes de archivos y 
					  # crear nuevas imágenes.Image

from PIL import ImageFilter # Contiene definiciones para un conjunto 
							# predefinido de filtros, que pueden usarse 
							# con el Image.filter()método.

try:
	img = Image.open("imagenes/KDA.jpg") # Abre e identifica el archivo de imagen dado.
										 # (Esta es una operación "perezosa": esta función 
										 # identifica el archivo, pero el archivo permanece 
										 # abierto y los datos de la imagen real no se leen 
										 # del archivo hasta que intenta procesar los datos.)

	print (img.mode) #Modo de imagen. Esta es una cadena que especifica el formato de píxel 
					 #utilizado por la imagen. Los valores típicos son "1", "L", "RGB" o "CMYK".

	print (img.getpixel((100,200))) #Devuelve el valor de píxel en una posición dada.
									#Parámetros:	xy - La coordenada, dada como 
									#(x, y). Ver sistema de coordenadas .
									#Devoluciones:	El valor de píxel. Si la imagen es 
									#una imagen de múltiples capas, este método devuelve una tupla.

	img = img.convert("CMYK") #Convierte la imagen en CMYK (Píxeles de 4x8 bits, separación de colores).

	img = img.rotate(20, expand = True) # Devuelve una copia rotada de esta imagen. Este método devuelve
										# una copia de esta imagen, giró el número dado de grados en 
										# sentido contrario a las agujas del reloj alrededor de su centro.
										# Parámetros: angle, resaple, expand, center, translate, fillcolor.

	img = img.transpose(Image.ROTATE_90) # Transponer imagen (voltear o rotar en pasos de 90 grados)
										 # Parámetros:	Método - Uno de PIL.Image.FLIP_LEFT_RIGHT, 
										 # PIL.Image.FLIP_TOP_BOTTOM, PIL.Image.ROTATE_90, 
										 # PIL.Image.ROTATE_180, PIL.Image.ROTATE_270, PIL.Image.TRANSPOSE 
										 # o PIL.Image.TRANSVERSE.
										 # Devoluciones:	Devuelve una copia volteada o girada de esta imagen.
	
	print (img.size) # Tamaño de la imagen, en píxeles. El tamaño se da como un 2-tupla (ancho, alto).
	
	ancho = int(img.width/2) # Ancho de la imagen, en píxeles.
	
	alto = int(img.height/2) # Alto de la imagen, en pixeles.

	img = img.resize((ancho,alto)) # Devuelve una copia redimensionada de esta imagen. (size, resample, box).

	box = (0,0,900,900) # Guarda una tupla.

	img = img.crop(box) # Devuelve una región rectangular de esta imagen. El cuadro es una tupla de 4 que 
						# define las coordenadas de píxel izquierdo, superior, derecho e inferior.

	copy = img.resize((1000,500)) # Devuelve una copia redimensionada de esta imagen y la guarda en la variable.

	ing = img.paste(copy, (100,100)) # Pega otra imagen en esta imagen. El argumento de cuadro es una tupla de 
									 # 2 que da la esquina superior izquierda, una tupla de 4 que define la 
									 # coordenada de píxel izquierda, superior, derecha e inferior, o Ninguna 
									 # (igual que (0, 0)).

	img = img.filter(ImageFilter.SMOOTH) # Contiene definiciones para un conjunto predefinido de filtros, que 
										 # pueden usarse con el Image.filter()método.

	img.show() # Muestra esta imagen. Este método está destinado principalmente para fines de depuración.
			   # En las plataformas Unix, este método guarda la imagen en un archivo PPM temporal y llama
			   # a la utilidad xv o la utilidad de visualización , dependiendo de cuál se pueda encontrar.
			   # En macOS, este método guarda la imagen en un archivo BMP temporal y la abre con la 
			   # aplicación de vista previa nativa.
			   # En Windows, guarda la imagen en un archivo BMP temporal y utiliza la utilidad de 
			   # visualización BMP estándar para mostrarla (normalmente Paint).

	img.save("nuevas/KDA.jpg") # Guarda esta imagen bajo el nombre de archivo dado. Si no se especifica ningún 
							   # formato, el formato a utilizar se determina a partir de la extensión del 
							   # nombre de archivo, si es posible.

except IOError:

	print("No se encontro la imagen.")