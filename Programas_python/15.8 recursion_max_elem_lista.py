def max_elem(lista):
	if lista==[]:
		return None
	return max_elem_recursivo(lista,lista[0])
	
def max_elem_recursivo(lista,elem):
	if lista==[]:
		return elem
	if lista[0]<=elem:
		return max_elem_recursivo(lista[1:],elem)
	return max_elem_recursivo(lista[1:],lista[0])
	
print(max_elem([4,5,6,7,8,9,15,5,9,195,0,-5,8]))
print(max_elem(['hola','fer','Hola','z','ZOrro','mama','A','a']))
	

	
	
