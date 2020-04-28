def head(n,ruta):
	with open (ruta,'r') as archivo:
		for linea in range(n):
			linea=archivo.readline()
			print(linea)
			
head(6,'texto.txt')

