from lista_enlazada import ListaEnlazada
from clase_nodo impor Nodo

def suma_acumulativa(self,numero_nodo):
	lista_nueva=ListaEnlazada()
	if self.primero is None:
		raise ValueError('lista esta vacia')
	else:
		while not self.primero.siguiente is None:
			valor=self.primero.contiene
			lista_nueva.append(valor)
			self.primero=self.primero.siguiente
			if self.primero.siguiente is None:
				valor=self.primero.contiene
				lista_nueva.append(valor)
				return lista_nueva
			self.primero.siguiente=self.primero.siguiente
			
		
			
