def es_par(n):
	if n==1:
		return False
	return es_impar(n-1)
		
def es_impar(n):
	if n==1:
		return True
	return es_par(n-1)
	
	
print(es_par(51))
print(es_par(50))
print(es_par(8))
print(es_par(9))
	
