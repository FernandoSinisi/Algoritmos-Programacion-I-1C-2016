def pedir_cant_num():
	m = int(input('Introduzca la cantidad de numeros a calcularle el factorial: '))
	return m

def pedir_num():
	numero = int(input('Introduzca el numero a calcularle el factorial: '))
	return numero

def calcular_factorial(numero):
	fac=1
	for x in range ( 1, numero+1):
		fac= x*fac
	return fac

def main():
	m = pedir_cant_num()
	for x in range(1,m+1):
		x=x+1
		numero = pedir_num()
		#factorial = calcular_factorial(numero)
		print( 'El factorial de {} es: {}'.format(numero,calcular_factorial(numero)))

main()


