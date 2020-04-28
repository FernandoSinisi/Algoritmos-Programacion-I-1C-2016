def imprimir_primeros_triangulares(cantidad):
	for n in range(1,cantidad+1):
		print('{} - {}'.format(n,calcular_triangular(n)))

def calcular_triangular(numero):
	return int(numero*(numero+1)/2)

imprimir_primeros_triangulares(5)

