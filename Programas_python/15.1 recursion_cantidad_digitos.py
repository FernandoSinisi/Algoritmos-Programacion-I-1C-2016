def cantidad_digitos(n):
	numero=str(n)
	if len(numero)==1:
		return 1
	return cantidad_digitos(numero[:-1])+1
	
print(cantidad_digitos(15638))
