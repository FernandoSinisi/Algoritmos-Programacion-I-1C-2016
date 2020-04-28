from clase_pila import Pila
def reemplazar(pila,viejo,nuevo):
	pila_aux=Pila()
	if pila.esta_vacia():
		raise ValueError('La pila esta vacia')
	while not pila.esta_vacia():
		dato=pila.desapilar()
		if dato==viejo:
			pila_aux.apilar(nuevo)
		else:
			pila_aux.apilar(dato)
	while not pila_aux.esta_vacia():
		dato_pasar=pila_aux.desapilar()
		pila.apilar(dato_pasar)
		

pila=Pila()
pila.apilar(5)
pila.apilar(3)
pila.apilar(3)
pila.apilar(4)
reemplazar(pila,3,8)
print(pila)
		
		
			
