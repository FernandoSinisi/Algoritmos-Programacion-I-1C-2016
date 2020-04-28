def es_potencia(n,b):
	'''precondicion n y b enteros,devuelve true si n es potencia de b,
	de loc contrario devuelve false'''
	if n<1:
		return False
	if n==1:
		return True
	return es_potencia(n/b,b)
	
print(es_potencia(16,4))
print(es_potencia(17,4))
print(es_potencia(125,5))
print(es_potencia(0,4))
print(es_potencia(1,4))	
print(es_potencia(0,0))
