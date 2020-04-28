def pedir_hs_minu_seg():
	print('Primer intervalo de tiempo')
	hs1=int(input('Ingrese la cantidad de horas: '))
	minu1=int(input('Ingrese la cantidad de minutos: '))
	seg1=int(input('Ingrese la cantidad de segundos: '))
	print('Segundo intervalo de tiempo')
	hs2=int(input('Ingrese la cantidad de horas: '))
	minu2=int(input('Ingrese la cantidad de minutos: '))
	seg2=int(input('Ingrese la cantidad de segundos: '))
	return hs1,hs2,minu1,minu2,seg1,seg2

def convertir_y_sumar_en_segundos():
	hs1,hs2,minu1,minu2,seg1,seg2=pedir_hs_minu_seg()
	return 3600*(hs1+hs2)+60*(minu1+minu2)+seg1+seg2

def convertir_a_hs_min_seg():
	seg_tot=convertir_y_sumar_en_segundos()
	horas=int(seg_tot/3600)
	minutos=int((seg_tot-(horas*3600))/60)
	segundos=seg_tot-(horas*3600)-(minutos*60)
	print('La suma de los intervalos son: {} horas, {} minutos, {} segundos'.format(horas,minutos,segundos))

	
convertir_a_hs_min_seg()

