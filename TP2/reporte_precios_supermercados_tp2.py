import csv
SUPERMERCADOS="supermercados.csv"
PRODUCTOS="productos.csv"
PRECIOS="precios.csv"

def abrir_archivo_4(ruta):
	lista_archivo_precio=[]
	with open (ruta) as archivo:
		archivo_csv=csv.reader(archivo)
		referencias=next(archivo_csv)
		while(True):
			try:
				for sup,prod,periodo,precio in archivo_csv:
					lista_archivo_precio.append((sup,prod,periodo,precio))
				#print(lista_archivo_precio)###########
				return lista_archivo_precio
			except:
				next(archivo_csv)
			
def abrir_archivo(ruta):
	dicc_super={}
	dicc_produ={}
	with open (ruta) as archivo:
		archivo_csv=csv.reader(archivo)
		referencias=next(archivo_csv)
		while(True):
			try:
				for num,item in archivo_csv:
					cont_super=int(num)
					if(ruta==SUPERMERCADOS):
						dicc_super[num]=item
					elif(ruta==PRODUCTOS):
						dicc_produ[num]=item
				if(ruta==SUPERMERCADOS):
					return dicc_super
				return dicc_produ			
			except:
				next(archivo_csv)
				
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
	
def validar_eleccion():
	opcion=pedir_eleccion()
	while True:
		for numero in range(1,6):
			if opcion!=str(numero):
				continue
			return opcion
		print('La opcion ingresada no es correcta')
		opcion=pedir_eleccion()
		
def pedir_periodo(momento):
	mes=input('Ingrese el numero del mes de {} del periodo (ejemplo: 06):  '.format(momento))
	año=input('Ingrese el numero del año de {} del periodo (ejemplo: 2015):  '.format(momento))
	return mes,año
	
def validar_periodo():
	mes,año=pedir_periodo(momento)
	if len(mes)==1:
		mes='0'+mes
	while(not mes.isdigit or not año.isdigit or len(año)!=4 or len(mes)!=2):
		print('Los datos ingresados no son validos')
		mes,año=pedir_periodo(momento)
	return mes,año
	
def verificar_periodo(lista_precios):
	mes,año=validar_periodo(momento)
	while True:
		periodo=año+mes
		for x in range (len(lista_precios)):
			if periodo in lista_precios[x][2]:
				return periodo
		print('El periodo escogido no esta contemplado, elija uno de 2015/2016')
		mes,año=validar_periodo(momento)		
		
	
	
def calcular_inflacion(precio_final,precio_inicial):
	return 100*((precio_final-precio_inicial)/precio_inicial)
	
def pedir_producto():
	producto=input('Ingrese el nombre del producto: ')
	return producto
	
def validar_producto(dicc_produ):
	lista_productos_posibles=[]
	producto=pedir_producto()
	while True:
		for x in range (1,len(dicc_produ)+1):
			if producto in dicc_produ[str(x)]:
				lista_productos_posibles.append(dicc_produ[str(x)]
		if lista_productos_posibles!=[]:
			return lista_productos_posibles
		print('No se encontró ningún producto con nombre {} '.format(producto))
		producto=pedir_producto()
	
	
main()
