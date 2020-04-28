import random
def dicci_numeros_suma_dados(tiradas):
	diccionario={}
	for x in range(tiradas):
		dado1=random.randrange(1,7)
		dado2=random.randrange(1,7)
		suma_dados=dado1+dado2
		if suma_dados in diccionario:
			diccionario[suma_dados]+=1
			continue
		diccionario[suma_dados]=1	
	return diccionario
	
dicci_numeros_suma_dados(5)

