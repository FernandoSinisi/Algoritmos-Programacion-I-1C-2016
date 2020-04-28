def imprimir_tablero(n):
	lista=[' ']
	abecedario=('a','b','c','d','e','f','g','h','i','j','k','l',"m","n","o","p","q","r","s","t","u","v","w","x","y","z")
	for i in range(n):
		lista.append('|')
	print('   ',end='')
	for numero_letra in range(n):
		print('  '+abecedario[numero_letra],end=' ')
	print('')
	for x in range(1,n+1):
		if x<10:
			print('0'+str(x),'|',end='')
		else:
			print(x,end='')
		for y in range(1,n+1):
			print ('_',lista[y],end='_')
		print (' ')
		

imprimir_tablero(6)
