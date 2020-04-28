import string
DIMENSION=8
USUARIO_1='B'
USUARIO_2='N'
ABECEDARIO=list(string.ascii_uppercase)
CANTIDAD_TURNOS=60

def saludo_bienvenida():
	"""Les da el saludo de bienvenida a los usuarios"""
	print('     Bienvenidos al Reversi')
	print('')
	
def crear_tablero_inicial(DIMENSION):
	tablero=[]
	for x in range(DIMENSION):
		tablero.append([' ']*DIMENSION)
	tablero[int(DIMENSION/2)-1][int(DIMENSION/2)-1]='B'
	tablero[int(DIMENSION/2)-1][int(DIMENSION/2)]='N'
	tablero[int(DIMENSION/2)][int(DIMENSION/2)-1]='N'
	tablero[int(DIMENSION/2)][int(DIMENSION/2)]='B'
	return tablero
	
def imprimir_tablero(tablero):
	print('  ',end='')
	for numero_letra in range(DIMENSION):
		print('  '+ABECEDARIO[numero_letra],end='')
	print('')
	for fila in range(DIMENSION):
		if fila<10:
			print('0'+str(fila),end='')
		else:
			print(fila,end='')
		for columna in range(DIMENSION):
			print(' |{}'.format(tablero[fila][columna]),end='')
		print(' |')
	print()
	
def esta_en_tablero(fila,columna):
	return (fila<DIMENSION and fila>=0 and columna<DIMENSION and columna>=0)
		
def hay_jugada_posible(fila,columna,usuario,tablero):
	ficha=usuario
	ficha_a_convertir_en_mia=[]
	if (ficha=='N'):
		ficha_otro_usuario='B'
	else: 
		ficha_otro_usuario='N'
	if not(es_valida_la_posicion(fila,columna,tablero)):
		return False
	for x in range(1,-2,-1):
		for y in range(1,-2,-1):
			if not(x==0 and y==0):
				fil=fila+x
				col=columna+y
				if (esta_en_tablero(fil,col) and tablero[fil][col]==ficha_otro_usuario):
					ficha_a_convertir_en_mia.append([fil,col])
					fil=fil+x  
					col=col+y
					if not(esta_en_tablero(fil,col)):
						ficha_a_convertir_en_mia=[]  
						continue  
					while (tablero[fil][col]==ficha_otro_usuario):
						ficha_a_convertir_en_mia.append([fil,col])
						fil=fil+x
						col=col+x  
						if not(esta_en_tablero(fil,col)): 
							break  
					if not(esta_en_tablero(fil,col)): 
						ficha_a_convertir_en_mia=[]
						continue   
					if(tablero[fil][col]==' '):
						ficha_a_convertir_en_mia=[]
						continue
					
	if(ficha_a_convertir_en_mia==[]):
		return False
	return ficha_a_convertir_en_mia  
		
def ingresar_datos_jugador():
	posicion_fila=(input('Ingrese el numero de la fila donde quiere colocar su ficha y presione enter: '))
	posicion_columna=input('Ingrese la letra de la columna donde quiere colocar su ficha y presione enter: ').upper()
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
	return fila,columna
	
def es_valida_la_posicion(fila,columna,tablero):
	return (tablero[fila][columna]==' ' and esta_en_tablero(fila,columna))
		
def todas_jugadas_posibles(usuario,tablero):
	for pos_fila in range(DIMENSION):
		for pos_col in range(DIMENSION):
			if(hay_jugada_posible(pos_fila,pos_col,usuario,tablero)!=False):
				return True
	return False
	
def colocar_ficha(tablero,usuario):
	fila,columna=validar_datos_jugador()
	while(hay_jugada_posible(fila,columna,usuario,tablero)==False):
		print('No hay jugada posible en esa posicion')
		fila,columna=validar_datos_jugador()
	for x,y in hay_jugada_posible(fila,columna,usuario,tablero):
		tablero[x][y]=usuario
	tablero[fila][columna]=usuario
	
		
def es_par(numero):
	return (numero%2==0)
		
def ciclo_de_juego(tablero,usuario):
	print('Es el turno del jugador: ',usuario)
	colocar_ficha(tablero,usuario)
	imprimir_tablero(tablero)
	
		
def main():
	saludo_bienvenida()
	while True:
		tablero=crear_tablero_inicial(DIMENSION)
		imprimir_tablero(tablero)
		turno=0
		while (turno<CANTIDAD_TURNOS):
			if (es_par(turno) and turno<CANTIDAD_TURNOS):
				ciclo_de_juego(tablero,USUARIO_2)
				turno=turno+1
			else:
				ciclo_de_juego(tablero,USUARIO_1)
				turno=turno+1
				
                

main()
	

	
