from clase_nodo import Nodo

class Cola:
	def __init__(self):
		self.primero=None
		self.ultimo=None
	def esta_vacia(self):
		return self.primero==None
	def encolar(self,valor):
		nuevo_nodo=Nodo(valor)
		if self.ultimo is not None:
			self.ultimo.siguiente=nuevo_nodo
			self.ultimo=nuevo_nodo
		else:
			self.primero=nuevo_nodo
			self.ultimo=nuevo_nodo
	def desencolar(self):
		if self.primero is None:
			raise ValueError('la cola esta vacia')
		else:
			dato=self.primero.contiene
			self.primero=self.primero.siguiente
			if self.primero is None:
				self.ultimo=None
		return dato
		
		
			

		
