from clase_cola import Cola
from clase_nodo import Nodo

cola=Cola()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
cola.encolar(4)

class ColaPrueba:
	def __init__(self,lista=[]):
		cola_de_reproduccion=Cola()
		for cancion in lista:
			cola_de_reproduccion.encolar(cancion)
		self.primero=cola_de_reproduccion.primero
		self.ultimo=cola_de_reproduccion.ultimo
		self.actual=cola_de_reproduccion.primero
	def remover_numero(self,numero):
		if self.primero is None:
			return False
		posicion=self.primero
		if posicion.contiene==numero:
			posicion.siguiente.anterior=None
			self.primero=posicion.siguiente
			return True
		while posicion.contiene!=numero:
			if not posicion.siguiente is None:
				posicion=posicion.siguiente
			else:
				return False
		posicion.anterior.siguiente=posicion.siguiente
		posicion.siguiente.anterior=posicion.anterior
		posicion=posicion.siguiente
		return True
	def cambiar_numero(self,numero):
		self.remover_numero(numero)

lista=[1,2,3,4,5]
cola_prueba=ColaPrueba(lista)
print(cola_prueba.primero)
print(cola_prueba.primero.siguiente)
print(cola_prueba.primero.siguiente.siguiente)
print(cola_prueba.primero.siguiente.siguiente.siguiente)
print(cola_prueba.primero.siguiente.siguiente.siguiente.siguiente)
cola_prueba.cambiar_numero(3)
print(cola_prueba.primero)
print(cola_prueba.primero.siguiente)
print(cola_prueba.primero.siguiente.siguiente)
print(cola_prueba.primero.siguiente.siguiente.siguiente)
print(cola_prueba.primero.siguiente.siguiente.siguiente.siguiente)
cola_prueba.cambiar_numero(5)
print(cola_prueba.primero)
print(cola_prueba.primero.siguiente)
print(cola_prueba.primero.siguiente.siguiente)
print(cola_prueba.primero.siguiente.siguiente.siguiente)
print(cola_prueba.primero.siguiente.anterior)

