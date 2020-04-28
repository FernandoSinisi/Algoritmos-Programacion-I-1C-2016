def convertir_cadena(cadena):
	'''Programa que dice si una cadena es palindromo o no'''
	cad=cadena.lower()
	posi_espa=0
	while (posi_espa!=-1):
		posi_espa=cad.find(' ')
		if (posi_espa==-1):
			return cad
		else:
			cad=cad[:posi_espa]+cad[posi_espa+1:]

def es_palindromo(cadena):
	if (convertir_cadena(cadena)==convertir_cadena(cadena)[::-1]):
		return True
	return False


