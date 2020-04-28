def es_primo(numero):
	if (numero<2):
		return False
	elif (numero==2 or numero==3):
		return True
	for x in range(2,numero-1):
		if numero%x==0:
			return False
		return True

	
es_primo(3)

