import os

from cancion import Cancion
from clase_nodo import Nodo
from clase_cola import Cola
from clase_pila import Pila


EXTENSIONES_ACEPTADAS = ("wav", "mp3", "flac", "ogg", "wma")

class ColaDeReproduccion:
	"""Clase que representa la cola de reproduccion del reproductor. Permite agregar y remover 
	canciones, ademas de poder hacer y deshacer estas acciones. Las canciones se guardan en la 
	cola como objetos de clase Cancion."""
	
	def __init__(self, lista_canciones = []):
		""" Recibe una lista de objetos de clase Cancion con las canciones que se quieren 
		reproducir."""
		cola_de_reproduccion=Cola()
		self.modificacion_cola=None
		self.accion_deshecha=None
		for cancion in lista_canciones:
			cola_de_reproduccion.encolar(cancion)
		self.primero=cola_de_reproduccion.primero
		self.ultimo=cola_de_reproduccion.ultimo
		self.actual=cola_de_reproduccion.primero

	def cancion_actual(self):
		""" Devuelve un objeto de clase Cancion que corresponde a la cancion actual, o None si no 
		hay canciones cargadas en la cola."""
		if self.actual is None:
			return None
		cancion=self.actual.contiene
		return cancion

	def cancion_siguiente(self):
		""" Devuelve un objeto de clase Cancion que corresponde a la cancion siguiente en la cola, 
		o None si no hay mas canciones."""
		if self.actual.siguiente is None:
			return None
		cancion=self.actual.siguiente.contiene
		self.actual=self.actual.siguiente
		return cancion

	def cancion_anterior(self):
		""" Devuelve un objeto de clase Cancion que corresponde a la cancion anterior en la cola, 
		o None si no hay canciones en la misma o la actual es la primera de la cola."""
		if self.actual==None  or self.actual.anterior==None:
			return None
		cancion=self.actual.anterior.contiene
		self.actual=self.actual.anterior

	def agregar_cancion(self, ruta_cancion):
		""" Agrega una Cancion a la cola a partir de su ruta. Devuelve True si se agrego 
		correctamente, False en caso contrario. Esta accion puede deshacerse y rehacerse."""
		try:
			cancion=Cancion(ruta_cancion)
			cola_de_reproduccion.encolar(cancion)
			self.modificacion_cola=('add',ruta_cancion)
			return True
		except:
			return False

	def remover_cancion(self, ruta_cancion):
		""" Remueve una Cancion de la cola a partir de su ruta. Devuelve True si se removio 
		correctamente, False en caso contrario. Esta accion puede deshacerse y rehacerse."""
		try:
			if self.primero is None:
				return False
			posicion=self.primero
			while posicion.contiene!=Cancion(ruta_cancion):
				if not posicion.siguiente is None:
					posicion=posicion.siguiente
				else:
					return False
			if posicion.anterior is None:
				posicion.siguiente.anterior=None
				self.primero=posicion.siguiente
				self.modificacion_cola('del',ruta_cancion)
				return True
			if posicion.siguiente is None:
				posicion.anterior.siguiente=posicion.siguiente
				posicion=posicion.siguiente
				self.modificacion_cola('del',ruta_cancion)
				return True
			posicion.anterior.siguiente=posicion.siguiente
			posicion.siguiente.anterior=posicion.anterior
			posicion=posicion.siguiente
			self.modificacion_cola('del',ruta_cancion)
			return True
		except:
			return False
			
	def deshacer_modificacion(self):
		""" Deshace la ultima accion realizada. Devuelve True si pudo deshacerse, False en caso 
		contrario."""
		if self.modificacion_cola==None:
			return False
		if self.modificacion_cola[0]=='add':
			self.remover_cancion(modificacion_cola[1])
			self.accion_deshecha=('add',modificacion_cola[1])
			self.modificacion_cola=None
			return True
		self.agregar_cancion(modificacion_cola[1])
		self.accion_deshecha=('del',modificacion_cola[1])
		self.modificacion_cola=None
		return True
		

	def rehacer_modificacion(self):
		""" Rehace la ultima accion que se deshizo. Devuelve True si pudo rehacerse, False en caso 
		contrario."""
		if accion_deshecha==None:
			return False
		if accion_deshecha[0]=='add':
			self.agregar_cancion(accion_deshecha[1])
			self.accion_deshecha=None
			return True
		self.remover_cancion(accion_deshecha[1])
		self.accion_deshecha=None
			
			

	def obtener_n_siguientes(self, n_canciones):
		""" Devuelve una lista con las siguientes n canciones. Si en la cola de reproduccion 
		quedan menos canciones que las pedidas, la lista contendra menos elementos que los 
		pedidos."""
		lista_canciones_siguientes=[]
		contador=0
		actual=self.actual
		while actual.siguiente!=None and contador<n_canciones:
			cancion=actual.siguiente.contiene
			lista_canciones_siguientes.append(cancion)
			actual=actual.siguiente
			contador+=1
		return lista_canciones_siguientes
