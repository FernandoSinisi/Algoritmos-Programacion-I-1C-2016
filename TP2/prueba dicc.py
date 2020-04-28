import csv
SUPERMERCADOS="supermercados.csv"
PRODUCTOS="productos.csv"
PRECIOS="precios.csv"
def abrir_archivo_precios(ruta):
	'''Funcion que recibe una ruta de un archivo de formato csv con 4 campos, lo lee y devuelve un diccionario
	con claves tuplas y valores asociados que son listas'''
	diccionario={}
	try:
		with open (ruta) as archivo:
			archivo_csv=csv.reader(archivo)
			referencias=next(archivo_csv)
			while True:
				try:
					for ind_sup,ind_prod,fecha,precio in archivo_csv:
						clave=(ind_sup,ind_prod)
						if clave in diccionario:
							diccionario[clave].append((fecha,precio))
							continue
						diccionario[clave]=[(fecha,precio)]
					return diccionario
				except:
					next(archivo_csv)
	except IOError:
		print("Se ha producido un error al buscar/leer el archivo ")
		
diccionario=abrir_archivo_precios(PRECIOS)
print(diccionario[('1','1')])
print(len(diccionario[('1','1')]))
print(len(diccionario))
print(diccionario[('1','1')][0][0])
		

		

