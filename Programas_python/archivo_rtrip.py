def leer(nombre):
	with open(nombre) as archivo:
		i = 1
		for linea in archivo:
			linea = linea.rstrip("\n")
			print("{}: {}".format(i, linea))
			i += 1
			
leer('texto.txt')
