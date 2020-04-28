Python 3.4.3 (default, Mar 26 2015, 22:07:01) 
[GCC 4.9.2] on linux
Type "copyright", "credits" or "license()" for more information.
>>> def convertir_y_sumar_en_segundos():
	hs1,hs2,minu1,minu2,seg1,seg2=pedir_hs_minu_seg()
	return 3600*(hs1+hs2)+60*(minu1+minu2)+seg1+seg2

>>> def pedir_hs_minu_seg():
	print('Primer intervalo de tiempo')
	hs1=int(input('Ingrese la cantidad de horas: '))
	minu1=int(input('Ingrese la cantidad de minutos: '))
	seg1=int(input('Ingrese la cantidad de segundos: '))
	print('Segundo intervalo de tiempo')
	hs2=int(input('Ingrese la cantidad de horas: '))
	minu2=int(input('Ingrese la cantidad de minutos: '))
	seg2=int(input('Ingrese la cantidad de segundos: '))
	return hs1,hs2,minu1,minu2,seg1,seg2

>>> def convertir_a_hs_min_seg(convertir_y_sumar_en_segundos())
	horas=int(convertir_y_sumar_en_segundos()/3600)
	minutos=int((convertir_y_sumar_en_segundos()-(horas*3600))/60)
	segundos=convertir_y_sumar_en_segundos()-(horas*3600)-(minutos*60)
	return horas, minutos, segundos
SyntaxError: invalid syntax
>>> def convertir_a_hs_min_seg(convertir_y_sumar_en_segundos())
	horas=int(convertir_y_sumar_en_segundos()/3600)
	minutos=int((convertir_y_sumar_en_segundos()-(horas*3600))/60)
	segundos=convertir_y_sumar_en_segundos()-(horas*3600)-(minutos*60)
	return horas, minutos, segundos
