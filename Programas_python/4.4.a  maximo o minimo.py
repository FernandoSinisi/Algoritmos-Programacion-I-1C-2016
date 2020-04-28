def es_maximo_o_minimo(a,b,c):
	if (a==0):
		print ('No es una funcion cuadratica')
	else:
		xv=-b/(2*a)
		yv=a*((-b/(2*a))**2)+b*(-b/(2*a))+c
		if (a<0):
			print('El valor es un maximo en {},{}'.format(xv,yv))
		else:
			print('El valor es un minimo en {},{}'.format(xv,yv))

			
es_maximo_o_minimo(1,0,2)

