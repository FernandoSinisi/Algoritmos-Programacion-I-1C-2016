def potencia(b,n):
	if n<=0:
		return 1
	if n%2==0:
		p=potencia(b,n/2)
		return p*p
	else:
		p=potencia(b,(n-1)/2)
		return p*p*b
		
print(potencia(5,3))

