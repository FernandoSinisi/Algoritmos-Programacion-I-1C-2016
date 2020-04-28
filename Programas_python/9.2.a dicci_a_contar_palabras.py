cadena_palabras='hola fer como estas fer contesta'
def dicci_para_contar(cadena):
	diccionario={}
	lista_de_palabras=cadena.split()
	for palabra in lista_de_palabras:
		if palabra in diccionario:
			diccionario[palabra]+=1
			continue
		diccionario[palabra]=1	
	return diccionario
	
dicci_para_contar(cadena_palabras)
