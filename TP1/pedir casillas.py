import string
DIMENSION=8
ABECEDARIO=list(string.ascii_uppercase)
def ingresar_datos_jugador():
	posicion_fila=(input('Ingrese el numero de la fila donde quiere colocar su ficha: '))
	posicion_columna=input('Ingrese la letra de la columna donde quiere colocar su ficha: ').upper()
	return posicion_fila,posicion_columna
	
def validar_datos_jugador():
	fila,columna=ingresar_datos_jugador()
	while(len(columna)!=1 or len(fila)>2 or not fila.isdigit() or not columna.isalpha()):
		print('Los datos ingresados no son correctos')
		fila,columna=ingresar_datos_jugador()
	columna=ABECEDARIO.index(columna)
	fila=int(fila)
	while not(esta_en_tablero(fila,columna)):
		print('Los datos ingresados no son correctos')
		fila,columna=ingresar_datos_jugador()
	print(fila,columna)
	return fila,columna


def esta_en_tablero(fila,columna):
	if	(fila<DIMENSION and fila>=0 and columna<DIMENSION and columna>=0):
		return True
	return False
			
		

	
validar_datos_jugador()

