def pascal(n,k):
	if k>n or n<0:
		print('tonto no se puede con ese numero')
	else:
		lista=nuevas_listas(n,k,[],0)
		print(lista[n][k])
	
def nuevas_listas(n,k,lista,cantidad):
	lista_interna=[]
	if cantidad==n+1:
		return lista
	else:
		for numeros in range(cantidad+1):
			if numeros==0 or numeros==cantidad:
				lista_interna.append(1)
			else:
				a=lista[cantidad-1][numeros-1]
				b=lista[cantidad-1][numeros]
				lista_interna.append(int(a)+int(b))
	cantidad+=1
	lista.append(lista_interna)
	return(nuevas_listas(n,k,lista,cantidad))
	
pascal(2,4)
pascal(0,0)
pascal(4,2)
pascal(15,19)
pascal(-1,-5)
	
