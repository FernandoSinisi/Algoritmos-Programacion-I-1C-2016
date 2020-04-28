from clase_pila import Pila
from clase_cola import Cola
from clase_nodo import Nodo
from lista_enlazada import ListaEnlazada

class TorreDeHanoi:
	def __init__(self):
		self.torre=Pila()
	def colocar_ficha(self,ficha):
		if self.torre.esta_vacia():
			self.torre.apilar(ficha)
		else:
			val_f_tope = self.torre.ver_tope().obtener_tamaño()
			val_f_colocar = ficha.obtener_tamaño()
			if val_f_colocar<val_f_tope:
				self.torre.apilar(ficha)
			else:
				raise ValueError('ficha de igual/mayor valor que la del tope de la torre')
	def sacarficha(self):
		if self.torre.esta_vacia():
			raise ValueError('Imposible sacar ficha, la torre esta vacia!!')
		else:
			return self.torre.desapilar()

def f(numero):
	return(numero%2==0)			

def filter_1(f):
	for numero in range(9):
		if f(numero):
			print('es par el numero {}'.format(numero))
		else:
			print('es impar el numero {}'.format(numero))
			
filter_1(f)

'''parcialito 3 rehacer filter y __mul__'''
def filter_(self,f):
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
					
lista=ListaEnlazada()
for numero in range(9):
	lista.append(numero)
print(lista.primero.contiene)
print(lista.primero.siguiente.contiene)
print(lista.primero.siguiente.siguiente.contiene)
print(lista.primero.siguiente.siguiente.siguiente.contiene)
print(lista.primero.siguiente.siguiente.siguiente.siguiente.contiene)
lista.filter_(f)
print(lista.primero.contiene)
print(lista.primero.siguiente.contiene)
print(lista.primero.siguiente.siguiente.contiene)
print(lista.primero.siguiente.siguiente.siguiente.contiene)
print(lista.primero.siguiente.siguiente.siguiente.siguiente.contiene)			
			
			
			
		
		
		

			
	


			
