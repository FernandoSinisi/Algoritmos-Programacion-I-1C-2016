def calcular_cap_final():
	cap_ini=float(input('Ingrese el capital inicial: '))
	tasa_int=int(input('Ingrese la tasa de interes: '))
	años=int(input('Ingrese los años: '))
	cap_fin = cap_ini*((1+tasa_int/100)**años)
	print ('El capital final es de ',cap_fin)

	
calcular_cap_final()


