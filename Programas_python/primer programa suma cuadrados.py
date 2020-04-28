def cuadrado(n):
	return n * n

def suma_cuadrados(n):
	suma = 0
	for x in range (1,n+1):
		suma = suma +cuadrado(x)
	return suma

def imprimir_suma_cuadrados(n):
	print('la suma de los primeros {} cuadrados es: {}'.format (n,suma_cuadrados(n)))
	
imprimir_suma_cuadrados(100)


