import os
EXTENSIONES_ACEPTADAS = ("wav", "mp3", "flac", "ogg", "wma")
directorio='/home/fs10/Documentos'
def funcion(directorio):
	lista_archivos=[]
	for ruta,lista_sub_rutas,lista_archivos in os.walk(directorio):
		for archivo in lista_archivos:
			print(os.path.join(ruta,archivo))
			extension=archivo.split('.')
			if extension[1]=='mp3':
					print('cargo_tema')
					
def agregar_canciones(ruta_directorio):
	""" Agrega a la cola las canciones que se encuentran en el directorio y en los directorios
	que se encuentran en el, recursivamente. Las extensiones aceptadas son las que se listan en 
	ColaDeReproduccion."""
	for ruta,subrutas,lista_archivos in os.walk(ruta_directorio):
		for archivo in lista_archivos:        #Itero todas las rutas de archivos del directorio y subdirectorios
			ruta_dato=os.path.join(ruta,archivo)
			extension=ruta_dato.split('.')
			if extension[-1] in EXTENSIONES_ACEPTADAS:
				print(ruta_dato)




agregar_canciones(directorio)


