def copiar_archivo(ruta):
	with open(ruta,'r') as archivo:
		datos=archivo.read()
		return datos

def crear_archivo_nuevo(ruta_nueva,ruta_vieja):
	with open (ruta_nueva,'w')as archivo:
		datos=copiar_archivo(ruta_vieja)
		archivo.write(datos)
		return archivo
		
crear_archivo_nuevo('texto_nuevo.txt','texto.txt')   ####crea texto nuevo iuji
		
	
