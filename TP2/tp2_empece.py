import csv
RUTA_SUPERMERCADOS='/home/fs10/Escritorio/TP2/supermecados.csv'
RUTA_PRODUCTOS='/home/fs10/Escritorio/TP2/productos.csv'
RUTA_PRECIOS='/home/fs10/Escritorio/TP2/precios.csv'

def crear_dicci(ruta):
	dicci_elem={}
	with open (ruta) as archivo:
		archivo_csv=csv.reader(archivo)
		next(archivo_csv)
		for indice,elem in archivo_csv:
			dicci_elem[indice]=(elem)
		print(dicci_elem)########################
		return dicci_elem
		
def mostrar_menu():
	print()
	print('        Menu principal')
	print('------------------------------')
	print('')
	print('1. Inflación por supermercado')
	print('2. Inflación por producto')
	print('3. Inflación general promedio')
	print('4. Mejor precio para un producto')
	print('5. Salir')

def pedir_eleccion():
	print()
	opcion=input('Escoja la opcion que desee: ')
	print()
	return opcion
	
def validar_opcion():
	opcion=pedir_eleccion()
	while True:
		for numero in range(1,6):
			if opcion!=str(numero):
				continue
			return opcion
		print('La opcion ingresada no es correcta')
		opcion=pedir_eleccion()
		
def pedir_periodo():
	mes_inicio=input('Ingrese el numero del mes de inicio del periodo. Ejemplo: 06 El mes escogido es:  ')
	año_inicio=input('Ingrese el numero del año de inicio del periodo. Ejemplo: 2015  El año escogido es:  ')
	mes_final=input('Ingrese el numero del mes del final del periodo. Ejemplo: 09 El mes escogido es:  ')
	año_final=input('Ingrese el numero del año del final del periodo. Ejemplo: 2016  El año escogido es:  ')
	return mes_inicio,año_inicio,mes_final,año_final

def calcular_inflacion(precio_final,precio_inicial):
	return 100*((precio_final-precio_inicial)/precio_inicial)
	
crear_dicci(RUTA_SUPERMERCADOS)



			

