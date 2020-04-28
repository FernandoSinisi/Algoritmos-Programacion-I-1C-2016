from clase_pila import Pila
def contar_elementos(pila):
	pila_original=pila
	pila_auxiliar=Pila()
	cantidad=0
	return contar_recursivo(pila_original,pila_auxiliar,cantidad)
	
def contar_recursivo(pila1,pila2,cant):
	if pila1.esta_vacia():
		for i in range(cant):
			pila1.apilar(pila2.desapilar())
		return cant
	else:
		pila2.apilar(pila1.desapilar())
		cant+=1
		return contar_recursivo(pila1,pila2,cant)
		
