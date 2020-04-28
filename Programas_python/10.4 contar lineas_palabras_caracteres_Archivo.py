def contar_partes_archivo(ruta):
	with open(ruta,'r') as archivo:
		cont_linea=0
		cont_palabras=0
		cont_caracteres=0
		for linea in archivo:
			cont_linea+=1
			lista_palabras=linea.split()
			cont_palabras+=len(lista_palabras)
			linea=linea.rstrip('\n')
			cont_caracteres+=len(linea)
		print('cantidad de lineas: '+str(cont_linea))
		print('cantidad de palabras: '+str(cont_palabras))
		print('cantidad de caracteres: '+str(cont_caracteres))
		
contar_partes_archivo('texto.txt')

