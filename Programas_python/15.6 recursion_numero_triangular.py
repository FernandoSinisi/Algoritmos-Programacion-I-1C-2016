def numero_triangular(n):
	if n==1:
		return 1
	return n+numero_triangular(n-1)
	
	
print(numero_triangular(1))
print(numero_triangular(2))
print(numero_triangular(3))
print(numero_triangular(4))

	

