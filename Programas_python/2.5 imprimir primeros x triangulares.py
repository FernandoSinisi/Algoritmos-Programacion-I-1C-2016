def imprimir_primeros_triangulares(cantidad):
	for n in range(1,cantidad+1):
		print('{} - {}'.format(n,calcular_triangular(n)))

def calcular_triangular(numero):
	resultado=0
	for i in range(1,numero+1):
		resultado+=i
	return resultado

def main(cantidad):
	imprimir_primeros_triangulares(cantidad)

	
main(5)

