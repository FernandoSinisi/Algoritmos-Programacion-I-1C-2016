def imprimir_numeros():
	'''recibe 2 numeros enteros e imprime en pantalla a los mismos mas todos los intermedios''' 
	numero_inicial = int(input('Ingrese el numero inicial: '))
	numero_final = int(input('Ingrese el numero final: '))
	serie = list(range (numero_inicial,numero_final+1,1))
	print (serie)

	
imprimir_numeros()

