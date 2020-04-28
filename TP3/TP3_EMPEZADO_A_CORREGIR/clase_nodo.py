class Nodo:
	def __init__(self,contiene,anterior=None,siguiente=None):
		self.contiene=contiene
		self.siguiente=siguiente
		self.anterior=anterior
	def __str__(self):
		return str(self.contiene)
