DIMENSION=8
USUARIO1='B'
USUARIO2='N'
def hay_jugada_posible(fila,columna,usuario,tablero):
	ficha=usuario
	ficha_a_convertir_en_mia=[]
	if (ficha=='N'):
		ficha_otro_usuario='B'
	else: 
		ficha_otro_usuario='N'
	
	if not(es_valida_la_posicion(fila,columna)):
		return False
	for x in range(1,-2,-1):
		for y in range(1,-2,-1):
			if not(x==0 and y==0):
				fil=fila+x
				col=columna+y
				if (esta_en_tablero(fil,col) and tablero[fil][col]==ficha_otro_usuario): #si al sumar x e y esta en tablero y es de otro usuario
					fil=fil+x  #sumo en la misma direccion
					col=col+y
					if not(esta_en_tablero(fil,col)):  #si no esta en tablero
						continue  # salta al otro x y del for
					while (tablero[fil][col]==ficha_otro_usuario):  # si es del otro usuario
						fil=fil+x
						col=col+x  #vuelve a sumar en la misma direccion siempre
						if not(esta_en_tablero(fil,col)): #pregunta si esta en tablero
							break  #frena el while
					if not(esta_en_tablero(fil,col)):  #cuando freno el while pregunta si no esta en tablero
						continue   #cambia al siguiente valor del for
					if(tablero[fil][col]==ficha):#pregunta si la ficha de esa posicion es la mia
						while True:  
							fil=fil-x  #volver para atras para guardar las posiciones donde paso
							col=col-y
							if (fil==fila and col==columna): # si llego a donde empece
								break  #frena el while
							ficha_a_convertir_en_mia.append([fil,col])  #agrega en lalista la posicion donde va a convertir
	if(ficha_a_convertir_en_mia==[]):  #si la lista es vacia no comio nada 
		return False  #no es jugada valida
	print(ficha_a_convertir_en_mia) #####
	return ficha_a_convertir_en_mia  #sino devuelve los lugares donde comio ficha
		
def esta_en_tablero(fila,columna):
	if	(fila<DIMENSION and fila>=0 and columna<DIMENSION and columna>=0):
		return True
	return False
			
	
def es_valida_la_posicion(fila,columna):
	tablero=crear_tablero(DIMENSION)
	if (tablero[fila][columna]==' ' and esta_en_tablero(fila,columna)):
		return True
	return False
	
	if (tablero[fila][columna]==' ' and esta_en_tablero(fila,columna)):
		return True
	return False
	
def crear_tablero(DIMENSION):
	tablero=[]
	for x in range(DIMENSION):
		tablero.append([' ']*DIMENSION)
	tablero[int(DIMENSION/2)-1][int(DIMENSION/2)-1]='B'
	tablero[int(DIMENSION/2)-1][int(DIMENSION/2)]='N'
	tablero[int(DIMENSION/2)][int(DIMENSION/2)-1]='N'
	tablero[int(DIMENSION/2)][int(DIMENSION/2)]='B'
	return tablero

hay_jugada_posible(5,3,USUARIO1,crear_tablero(DIMENSION))
