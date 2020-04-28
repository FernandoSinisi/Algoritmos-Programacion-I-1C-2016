dicci_1={'fer':'fs10','franco':'fds8','tony':'accs7','maria':'mes9','flor':8}
dicci_2={'fer':'fs10','tony':'accs7','franco':'fsd8','flor':'8','leonel':'no estaba'}
lista=[1,2,3,4,5,6,8,9,15,125,22]
lista_poli=[(0,9),(2,6),(5,9),(8,15)]
lista_poli2=[(0,9),(1,6),(2,6),(3,4),(4,1),(5,9)]

"""ejercicio 2 final"""

def diferencia(dic1,dic2):
	dicci_diff={}
	for clave in dic1:
		if not clave in dic2:
			dicci_diff[clave]=(dic1[clave],'')
			continue
		if dic1[clave]!=dic2[clave]:
			dicci_diff[clave]=(dic1[clave],dic2[clave])
	for clave in dic2:
		if not clave in dic1:
			dicci_diff[clave]=('',dic2[clave])
	return dicci_diff
	
	
otro=diferencia(dicci_1,dicci_2)
print('claves: ' + str(otro.keys()))
print('valores:' + str(otro.values()))

"""ejercicio 3 final"""

def lista_pares(lista):
	if len(lista)==0:
		return []
	if lista[0]%2==0:
		return [lista[0]]+ lista_pares(lista[1:])
	return lista_pares(lista[1:])
	
print(lista_pares(lista)) 
print(lista)

"""ejercicio 4 final"""

class Polinomio:
	def __init__(self,lista):
		self.grados=()
		self.coef=()
		for grado,coef in lista:
			self.grados+=(grado,)
			self.coef+=(coef,)
	def __str__(self):
		cadena=''
		for x in range(len(self.grados)):
			if self.grados[x]==0:			
				cadena+='{}'.format(self.coef[x])
			elif self.grados[x]==1:
				cadena+='+{}X'.format(self.coef[x])
			else:
				cadena+='+{}X^{}'.format(self.coef[x],self.grados[x])
		return cadena
	def suma(self,otro):
		lista1,cont1,cont2=([],0,0)
		while cont1<len(self.grados) and cont2<len(otro.grados):
			if self.grados[cont1]>otro.grados[cont2]:
				lista1.append((otro.grados[cont2],otro.coef[cont2]))
				cont2+=1
			elif self.grados[cont1]<otro.grados[cont2]:
				lista1.append((self.grados[cont1],self.coef[cont1]))
				cont1+=1
			else:
				lista1.append((self.grados[cont1],self.coef[cont1]+otro.coef[cont2]))
				cont1+=1
				cont2+=1
		if cont1==len(self.grados):
			for x in range(cont2,len(otro.grados)):
				lista1.append((otro.grados[x],otro.coef[x]))
		else:
			for x in range(cont1,len(self.grados)):
				lista1.append((self.grados[x],self.coef[x]))
		return Polinomio(lista1)
		

poli=Polinomio(lista_poli)
poli2=Polinomio(lista_poli2)
print(poli)
print(poli2)
print(poli.suma(poli2))

		
			
			
		







			
