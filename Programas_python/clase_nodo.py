class Nodo:
	def __init__(self,contiene,siguiente=None):
		self.siguiente=siguiente
		self.contiene=contiene
	def __str__(self):
		return str(self.contiene)
