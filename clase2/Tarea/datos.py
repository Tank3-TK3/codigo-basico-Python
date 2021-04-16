datos1 = "101;Johnny ‘wave-boy’ Jones;USA;8.32;Fish;21"
#print (cadena)
lista1 = datos1.split(";")
#print (lista1)
datos2 = "ID: ,Name: ,Country: ,Average: ,Board type: ,Age: "
lista2 = datos2.split(",")
#print (lista2)
matriz = [lista2[0]+lista1[0], lista2[1]+lista1[1], lista2[2]+lista1[2], lista2[3]+lista1[3], lista2[4]+lista1[4], lista2[5]+lista1[5]]
#print (matriz)
print (matriz[0])
print (matriz[1])
print (matriz[2])
print (matriz[3])
print (matriz[4])
print (matriz[5])