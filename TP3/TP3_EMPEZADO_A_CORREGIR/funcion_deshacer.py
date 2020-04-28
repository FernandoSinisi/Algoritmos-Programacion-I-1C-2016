class Pila:
	def __init__(self):
		self.items=[]
	def __str__(self):
		valor=""
		for elemento in self.items:
			valor+=str(elemento)+","
		return valor
	def apilar(self,x):
		self.items.append(x)
	def desapilar(self):
		if self.esta_vacia():
			raise ValueError("La pila esta vacia")
		return self.items.pop()
	def esta_vacia(self):
		return len(self.items)==0
	def ver_tope(self):
		if self.esta_vacia():
			return None
		return self.items[-1]

def agregar_comando(stack,comando):
	stack.apilar(comando)
		
def deshacer_comando(stack):
	if stack.esta_vacia():
		raise IndexError("No hay acciones anteriores")
	actual = stack.desapilar()
	return stack.ver_tope()

def main():
	stack=Pila()
	for comando in("Hola","Como estás?","Soy un comando","Agregar comando","Quitar comando","Reproducir ;)","Finalizar :("):
		agregar_comando(stack,comando)
	for i in range(3):
		print(deshacer_comando(stack))
main()
