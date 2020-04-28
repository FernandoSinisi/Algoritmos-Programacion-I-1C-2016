def imprimir_fichas_juego(n):
	for primer_numero in range (n+1):
		for segundo_numero in range (primer_numero,n+1):
			print('{}:{}'.format(primer_numero,segundo_numero))
			
imprimir_fichas_juego(5)




