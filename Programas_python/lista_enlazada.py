from clase_nodo import Nodo

class ListaEnlazada:
	def __init__(self):
		self.primero=None
		self.longitud=0
	def append(self,contenido):
		self.longitud+=1
		nodo_nuevo=Nodo(contenido)
		if not self.primero:
			self.primero=nodo_nuevo
		else:
			nodo=self.primero
			while nodo.siguiente:
				nodo=nodo.siguiente
			nodo.siguiente=nodo_nuevo
	def pop(self,posicion=None):
		if posicion==None:
			posicion=self.longitud-1
		if (posicion<0 or posicion>=self.longitud):
			raise IndexError('Posicion fuera de rango')
		if (posicion==0):
			contenido=self.primero.contiene
			self.primero=self.primero.siguiente
		else:
			anterior=self.primero
			actual=anterior.siguiente
			contador=0
			while contador<posicion-1:
				contador+=1
				anterior=actual
				actual=actual.siguiente
			contenido=actual.contiene
			actual.siguiente=actual.siguiente
		self.longitud-=1
		return contenido
	def invertir(self):
		if self.primero is None:
			print('la lista esta vacia, no se puede invertir')
			return None
		actual=self.primero
		anterior=None
		while actual:
			siguiente=actual.siguiente
			actual.siguiente=anterior
			anterior=actual
			actual=siguiente
		self.primero=anterior
	def remove(self,valor):
		if self.longitud==0:
			raise ValueError("Lista vacía")
		if self.primero.contiene==valor:
			self.primero=self.primero.siguiente
		else:
			anterior=self.primero
			actual= anterior.siguiente
			while actual is not None and actual.contiene!=valor:
				anterior=actual
				actual=anterior.siguiente
			if actual==None:
				raise ValueError("El valor no está en la lista.")
		anterior.siguiente=actual.siguiente
		self.longitud-=1
	def filter_(self,f):                  ##### metodo agregado para el parcialito para probarlo ###
		if self.primero is None:
			raise IndexError('Lista vacia')
		while not f(self.primero.contiene):
			self.primero=self.primero.siguiente
			if not self.primero:
				break
		if self.primero:
			anterior=self.primero
			actual=anterior.siguiente	
			while actual:
				if f(actual.contiene):
					anterior=actual
					actual=anterior.siguiente
				else:
					anterior.siguiente=actual.siguiente
					actual=anterior.siguiente

		
		

		
