'''Resolver recursivamente:
Dada una lista de enteros y un entero a 
devolver en una ista todas las posiciones en las que aparece a en la lista'''

lista=[3,6,8,9,3,7,6,5,2,1,10,81,9,1,8,7,6,3,8,5,4,6]

def aparicion(lista,valor):
	return aparicionx(lista,valor,0)
	
def aparicionx(lista,valor,posicion):
	if lista==[]:
		return []
	if lista[0]==valor:
		return [posicion]+aparicionx(lista[1:],valor,posicion+1)
	else:
		return aparicionx(lista[1:],valor,posicion+1)
		
print(aparicion(lista,3))



				


	
