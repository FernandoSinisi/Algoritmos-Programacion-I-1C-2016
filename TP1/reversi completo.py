import string
DIMENSION=4
USUARIO_1='B'
USUARIO_2='N'
ABECEDARIO=list(string.ascii_uppercase)
CANTIDAD_TURNOS=60

def saludo(palabra):
	"""Les da el saludo de bienvenida o despedida a los usuarios"""
	print('')
	if(palabra=='bienvenida'):
		print('           Bienvenidos al Reversi')
		print('')
	else:
		print('     Gracias por jugar al Reversi')
		print('')
	
def crear_tablero_inicial(DIMENSION):
	'''Recibe por parametro un numero y crea una lista de esa cantidad de
	   elementos, donde cada uno son listas con la cantidad de elementos de ese numero y la devuelve'''
	tablero=[]
	for x in range(DIMENSION):
		tablero.append([' ']*DIMENSION)
	tablero[int(DIMENSION/2)-1][int(DIMENSION/2)-1]='B'
	tablero[int(DIMENSION/2)-1][int(DIMENSION/2)]='N'
	tablero[int(DIMENSION/2)][int(DIMENSION/2)-1]='N'
	tablero[int(DIMENSION/2)][int(DIMENSION/2)]='B'
	return tablero
	
def imprimir_tablero(tablero):
	'''Recibe por parametro una lista de listas y la
		imprime por pantalla en forma de tablero'''
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
	'''Recibe por parametro 2 valores correspondientes a la fila y
	   columna del tablero y devuelve True/False segun este en el tablero'''
	return (fila<DIMENSION and fila>=0 and columna<DIMENSION and columna>=0)
		
def hay_jugada_posible(fila,columna,usuario,tablero):
	'''Recibe por parametro 4 valores: Una fila, una columna, el usuario
	   y el tablero, verifica si hay jugada posible, devolviendo una lista de 
	   las posiciones a comer por ese usuario, si la lista esta vacia devuelve False'''
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
				while(esta_en_tablero(fil,col) and tablero[fil][col]==ficha_otro_usuario):
					fil+=x  
					col+=y
					if not(esta_en_tablero(fil,col)):  
						break  
				if not(esta_en_tablero(fil,col)): 
						continue
				if(tablero[fil][col]==ficha): 
					while True:  
						fil-=x  
						col-=y
						if (fil==fila and col==columna): 
							break  
						ficha_a_convertir_en_mia.append([fil,col]) 
	if(ficha_a_convertir_en_mia==[]):
		return False
	return ficha_a_convertir_en_mia  
		
def ingresar_datos_jugador():
	'''Pide al usuario la fila y columna a donde quiere colocar su ficha y la devuelve'''
	posicion_fila=(input('Ingrese el numero de la fila donde quiere colocar su ficha y presione enter: '))
	posicion_columna=input('Ingrese la letra de la columna donde quiere colocar su ficha y presione enter: ').upper()
	return posicion_fila,posicion_columna
	
def validar_datos_jugador():
	'''Recibe del usuario la fila y columna, valida que esos datos sean correctos, si
	   lo son los devuelve, de lo contrario los pide de nuevo hasta que sean validos'''
	fila,columna=ingresar_datos_jugador()
	while(len(columna)!=1 or len(fila)>2 or not fila.isdigit() or not columna.isalpha()):
		print('Los datos ingresados no son correctos')
		print('')
		fila,columna=ingresar_datos_jugador()
	columna=ABECEDARIO.index(columna)
	fila=int(fila)
	while not(esta_en_tablero(fila,columna)):
		print('Los datos ingresados no son correctos')
		print('')
		fila,columna=ingresar_datos_jugador()
	return fila,columna
	
def es_valida_la_posicion(fila,columna,tablero):
	'''Recibe por parametro la fila,columna y tablero y devuelve True/False 
	   segun esa posicion este en el tablero y sea un caracter espacio'''
	return (tablero[fila][columna]==' ' and esta_en_tablero(fila,columna))
		
def todas_jugadas_posibles(usuario,tablero):
	'''Recibe por parametro el usuario y el tablero, lo recorre posicion por
	   posicion y devuelve True/False dependiendo si ese usuario tiene jugada posible'''
	for pos_fila in range(DIMENSION):
		for pos_col in range(DIMENSION):
			if(hay_jugada_posible(pos_fila,pos_col,usuario,tablero)!=False):
				return True
	return False
	
def colocar_ficha(tablero,usuario):
	'''Recibe por parametro el tablero y usuario,pide al usuario una fila y 
	columna y si hay jugada posible modifica el tablero colocando su ficha
	 en las posiciones correspondientes'''
	fila,columna=validar_datos_jugador()
	while(hay_jugada_posible(fila,columna,usuario,tablero)==False):
		print('No hay jugada posible en esa posicion')
		print('')
		fila,columna=validar_datos_jugador()
	for x,y in hay_jugada_posible(fila,columna,usuario,tablero):
		tablero[x][y]=usuario
	tablero[fila][columna]=usuario
	
def quien_gano(tablero):
	'''Recibe por parametro el tablero, lo recorre completo contando las fichas
	de cada usuario y devuelve el usuario que gano o False si es empate'''
	fichas_usuario_1=0
	fichas_usuario_2=0
	for fila in range(DIMENSION):
		for columna in range(DIMENSION):
			if(tablero[fila][columna]==USUARIO_1):
				fichas_usuario_1+=1
			elif(tablero[fila][columna]==USUARIO_2):
				fichas_usuario_2+=1
			else:
				continue
	if(fichas_usuario_1==fichas_usuario_2):
		return False
	elif (fichas_usuario_1>fichas_usuario_2):
		return USUARIO_1
	return USUARIO_2

def datos_volver_a_jugar():
	'''Pide al usuario un dato para saber que desea hacer y lo devuelve'''
	dato=input('si desea volver a jugar presione 1 / si desea salir presione 0: ')
	return dato
	
def validar_datos_volver_a_jugar():
	'''Recibe del usuario el dato,lo valida, si es correcto lo devuelve sino
	lo vuelve a pedir hasta que sea correcto'''
	caracter=datos_volver_a_jugar()
	while(caracter!='1' and caracter!='0'):
		print('El caracter ingresado no es correcto')
		print('')
		caracter=datos_volver_a_jugar()
	return caracter
	
def volver_a_jugar():
	'''Recibe el dato validado y devuelve True/False segun corresponda'''
	if(validar_datos_volver_a_jugar()=='1'):
		return False
	return True
	
def es_par(numero):
	'''Recibe un numero por parametro y devuelve True/False dependiendo
	 si el numero es par o no'''
	return (numero%2==0)
		
def ciclo_de_turno(tablero,usuario):
	'''Recibe por parametro el usuario y el tablero,imprime en pantalla de 
	quien es el turno, realiza la jugada e imprime el tablero modificado'''
	print('Es el turno del jugador: ',usuario)
	print('')
	if(todas_jugadas_posibles(usuario,tablero)):
		colocar_ficha(tablero,usuario)
		print('')
		imprimir_tablero(tablero)
	else:
		print('No tiene jugadas posible el jugador: ',usuario)
		print('')
			
def ciclo_del_juego():
	'''Imprime en pantalla el tablero inicial, va pasando los turnos de un usuario a otro e 
	    imprimiendo los nuevos tableros,verificando si se llego a los turnos maximos 
	    o si no hay jugadas posibles e imprime quien fue el ganador o si fue empate'''
	while True:
		tablero=crear_tablero_inicial(DIMENSION)
		print('')
		imprimir_tablero(tablero)
		turno=0
		while (turno<CANTIDAD_TURNOS and (todas_jugadas_posibles(USUARIO_1,tablero) or todas_jugadas_posibles(USUARIO_2,tablero))):
			while(es_par(turno)):
				ciclo_de_turno(tablero,USUARIO_2)
				turno+=1
			while not(es_par(turno)):		
					ciclo_de_turno(tablero,USUARIO_1)
					turno+=1
		if(turno==CANTIDAD_TURNOS):
			print('Llegaron a la cantidad maxima de turnos')
			print('')			
		else:
			print('Ninguno de los dos jugadores tiene jugadas posibles')
			print('')
		if (quien_gano(tablero)==False):
			print('¡¡¡¡EMPATE!!!!')
			PRINT('')
			break
		else:
			print('El jugador ganador fue: ',quien_gano(tablero))
			print('')
			break
	
def main():
	'''Funcion principal que saluda al usuario, ejecuta el juego, pregunta si 
	se desea volver a jugar, de lo contrario despide al usuario'''
	saludo('bienvenida')
	while True:
		ciclo_del_juego()
		if(volver_a_jugar()):
			break
	saludo('despedida')
		
	
main()
	

	
