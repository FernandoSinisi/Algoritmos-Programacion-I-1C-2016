def imprimir_pares(a,b):
	for par in range(a+a%2,b+1,2):
		print(par)

def pedir_entero(detalle):
	n=int(input('Introduzca un entero ({}):'.format(detalle)))
	return n

def main():
	lim_menor = pedir_entero('limite menor')
	lim_mayor = pedir_entero('limite mayor')
	imprimir_pares(lim_menor,lim_mayor)

	
main()



