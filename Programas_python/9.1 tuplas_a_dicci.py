lista=[('hola','fer'),('boca','juniors'),('riber','plate'),('boca','campeon'),('boca','puntero')]
def tuplas_a_dicci(lista_tuplas):
	dicci={}
	for x in range(len(lista_tuplas)):
		clave,valor=lista_tuplas[x]
		if clave in dicci:
			dicci[clave].append(valor)
		else:
			dicci[clave]=[valor]
	print(dicci)
	
tuplas_a_dicci(lista)

	
