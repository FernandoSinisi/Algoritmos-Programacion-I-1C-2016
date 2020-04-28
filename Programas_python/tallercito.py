'''Segundo recuperatorio 2015 tirangulito de numeros'''
def pascal(n,k):
	'''precondicion: n(filas),k(columnas) naturales +{0} y k<=n
	devuelve el pascal de (n,k)'''
	if k==0 or k==n:
		return 1
	return pascal(n-1,k)+pascal(n-1,k-1)
#falla para caso 0,2 hya que poner excepcion y mirar bien
#k>n  exception value
#n<0 exception value'''

#print(pascal(4,2))







