cadena_palabras='hola fer como estas fer contesta'
def dicci_para_contar(cadena):
	diccionario={}
	for caracter in cadena:
		if caracter in diccionario:
			diccionario[caracter]+=1
			continue
		diccionario[caracter]=1	
	return diccionario
	
dicci_para_contar(cadena_palabras)
