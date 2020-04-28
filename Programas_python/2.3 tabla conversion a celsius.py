
def convertir_a_celsius(temp_farenheit):
	'''funcion que convierte la temperatura en grados farenheit a grados celsius'''
	temp_celsius=(temp_farenheit-32)*(5/9)
	return temp_celsius

def imprimir_tabla_conversion():
	'''funcion que imprime tabla de conversión de temperaturas, desde 0 °F hasta 120 °F, de 10 en 10'''
	for temp_farenheit in range (0,121,10):
		temp_celsius= convertir_a_celsius(temp_farenheit)
		print('{} farenheit son {} celsius'.format(temp_farenheit,temp_celsius))

		
imprimir_tabla_conversion()




