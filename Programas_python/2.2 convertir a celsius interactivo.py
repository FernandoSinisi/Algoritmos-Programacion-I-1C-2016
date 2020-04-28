def convertir_a_celsius(temp_farenheit):
	return(temp_farenheit-32)*(5/9)
	
def convertir_a_celsius_interactivo():
	temp_farenheit=float(input('Ingrese la temperatura en farenheit: '))
	print ('{} grados farenheit son {} grados celsius'.format(temp_farenheit,convertir_a_celsius(temp_farenheit)))

	
convertir_a_celsius_interactivo()






