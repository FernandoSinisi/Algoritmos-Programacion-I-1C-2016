def convertir_a_hs_min_seg(seg):
	horas=int(seg/3600)
	minutos=int((seg-(horas*3600))/60)
	segundos=seg-(horas*3600)-(minutos*60)
	return horas, minutos, segundos
	

	

