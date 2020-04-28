eimport csv
SUPERMERCADOS="supermercados.csv"
PRODUCTOS="productos.csv"
PRECIOS="precios.csv"
INFLACION_POR_SUPERMERCADO=1
INFLACION_POR_PRODUCTO=2
INFLACION_GENERAL_PROMEDIO=3
MEJOR_PRECIO_PARA_UN_PRODUCTO=4
SALIR=5

def abrir_archivo_precios(ruta):
	'''Funcion que recibe una ruta de un archivo de fomrato csv, lo lee y devuelve una lista de tuplas,
	donde cada elemento de la tupla es una campo de la linea del archivo.'''
	lista_archivo_precio=[]
	try:
		with open (ruta) as archivo:
			archivo_csv=csv.reader(archivo)
			referencias=next(archivo_csv)
			while True:
				try:
					for sup,prod,periodo,precio in archivo_csv:
						lista_archivo_precio.append((sup,prod,periodo,precio))
					return lista_archivo_precio
				except:
					next(archivo_csv)
	except IOError:
		print("Se ha producido un error al buscar/leer el archivo ")
			
def abrir_archivo(ruta):
	'''Funcion que recibe una ruta de un archivo de formato csv, lo lee y devuelve un diccionario donde la clave
	es el indice y el valor es el producto o supermercado asociado a ese indice.'''
	dicc_super={}
	dicc_produ={}
	try:
		with open (ruta) as archivo:
			archivo_csv=csv.reader(archivo)
			referencias=next(archivo_csv)
			while True:
				try:
					for num,item in archivo_csv:
						indice=int(num)
						if(ruta==SUPERMERCADOS):
							dicc_super[num]=item.lower()
						elif(ruta==PRODUCTOS):
							dicc_produ[num]=item.lower()
					if(ruta==SUPERMERCADOS):
						return dicc_super
					return dicc_produ			
				except:
					next(archivo_csv)
	except IOError:
		print("Se ha producido un error al buscar/leer el archivo ")
		
def mostrar_menu():
	'''Funcion que muestra el menu principal del programa'''
	print()
	print('        Menu principal\n''------------------------------\n')
	print('1. Inflación por supermercado\n2. Inflación por producto')
	print('3. Inflación general promedio\n4. Mejor precio para un producto\n5. Salir\n')

def pedir_eleccion(mensaje):
	opcion=input('Escoja {} que desee: '.format(mensaje))
	return opcion
	
def validar_eleccion(mensaje):
	opcion=pedir_eleccion(mensaje)
	while True:
		for numero in range(1,6):
			if opcion!=str(numero):
				continue
			return int(opcion)
		print('La opcion ingresada no es correcta')
		opcion=pedir_eleccion(mensaje)

def imprimir_inflacion_por_supermercado(dicc_super,dicc_produ,lista_precios):
	fecha_ini=verificar_fecha(lista_precios,"inicial")
	fecha_fin=verificar_fecha(lista_precios,"final")
	infla_sup1,infla_sup2,infla_sup3=calcular_inflacion_super(lista_precios,fecha_ini,fecha_fin)
	print("La inflacion en el supermercado Coto en el periodo indicado fue: {:.3}%".format(infla_sup1))
	print("La inflacion en el supermercado Jumbo en el periodo indicado fue: {:.3}%".format(infla_sup2))
	print("La inflacion en el supermercado Carrefour en el periodo indicado fue: {:.3}%".format(infla_sup3))
		 
def calcular_inflacion_super(lista_precios,fecha_ini,fecha_fin):
	suma_precio_ini_1=0
	suma_precio_fin_1=0
	suma_precio_ini_2=0
	suma_precio_fin_2=0
	suma_precio_ini_3=0
	suma_precio_fin_3=0
	for elemento in range(len(lista_precios)):
		if(int(lista_precios[elemento][2])==fecha_ini):
			if(lista_precios[elemento][0]=="1"):
				suma_precio_ini_1+=float(lista_precios[elemento][3])
			elif(lista_precios[elemento][0]=="2"):
				suma_precio_ini_2+=float(lista_precios[elemento][3])
			elif(lista_precios[elemento][0]=="3"):
				suma_precio_ini_3+=float(lista_precios[elemento][3])
		elif(int(lista_precios[elemento][2])==fecha_fin):
			if(lista_precios[elemento][0]=="1"):
				suma_precio_fin_1+=float(lista_precios[elemento][3])
			elif(lista_precios[elemento][0]=="2"):
				suma_precio_fin_2+=float(lista_precios[elemento][3])
			elif(lista_precios[elemento][0]=="3"):
				suma_precio_fin_3+=float(lista_precios[elemento][3])
	inflacion_total_super_1=calcular_inflacion(suma_precio_fin_1,suma_precio_ini_1)
	inflacion_total_super_2=calcular_inflacion(suma_precio_fin_2,suma_precio_ini_2)
	inflacion_total_super_3=calcular_inflacion(suma_precio_fin_3,suma_precio_ini_3)
	return inflacion_total_super_1,inflacion_total_super_2,inflacion_total_super_3
		 
def inflacion_por_producto(dicc_super,dicc_produ,lista_precios):
	lista_prod_posibles=imprimir_productos_posibles(dicc_produ)
	indice_prod_lista_posibles=validar_eleccion_producto(lista_prod_posibles,"el numero de producto",1)
	producto=lista_prod_posibles[int(indice_prod_lista_posibles)-1]
	while True:
		print("El producto elegido es: {}".format(producto))
		es_correcto=input("Es el producto deseado(s/n):")
		es_correcto=es_correcto.lower()
		if(es_correcto=="s"):
			break
		elif(es_correcto=="n"):
			indice_prod_lista_posibles=validar_eleccion_producto(lista_prod_posibles,"el numero de producto",1)
			producto=lista_prod_posibles[int(indice_prod_lista_posibles)-1]
		print('Responda por si o por no con s/n')
	for valor in range(len(dicc_produ)):
		if (producto==dicc_produ[str(valor+1)]):
			indice_prod_dicc_produ=valor+1
			break
	fecha_ini=verificar_fecha(lista_precios," <Periodo inicial>")
	fecha_fin=verificar_fecha(lista_precios,"<Periodo final>")
	for x in range(1,len(dicc_super)+1):
		precio_inicial,precio_final=precio_ini_fin(str(x),lista_precios,indice_prod_dicc_produ,fecha_ini,fecha_fin)
		inflacion_sup=calcular_inflacion(precio_final,precio_inicial)
		print("La inflacion de {} en el supermercado {} fue: {:.3}%".format(producto,dicc_super[str(x)],inflacion_sup))
	
	

def precio_ini_fin(sm,lista_precios,indice_prod_dicc_produ,periodo_ini,periodo_fin):
	for j in range(len(lista_precios)):
		if (lista_precios[j][0]==sm):
			if(int(lista_precios[j][1])==indice_prod_dicc_produ):
				if(int(lista_precios[j][2])==periodo_ini):
					precio_ini_sup=float(lista_precios[j][3])
				elif(int(lista_precios[j][2])==periodo_fin):
					precio_fin_sup=float(lista_precios[j][3])
	return precio_ini_sup,precio_fin_sup	
	
def inflacion_general_promedio(dicc_super,dicc_produ,lista_precios):
	periodo_ini=verificar_fecha(lista_precios,"<Periodo inicial>")
	periodo_fin=verificar_fecha(lista_precios,"<Periodo final>")
	suma_precio_ini=0
	suma_precio_fin=0
	for x in range(len(lista_precios)):
		if(int(lista_precios[x][2])==periodo_ini):
			suma_precio_ini+=float(lista_precios[x][3])
		elif(int(lista_precios[x][2])==periodo_fin):
			suma_precio_fin+=float(lista_precios[x][3])
	infl_gral_promedio=calcular_inflacion(suma_precio_fin,suma_precio_ini)
	print("La inflacion general promedio de los tres sumermercados fue: {:.3}%".format(infl_gral_promedio))
	
def mejor_precio_para_un_producto(dicc_super,dicc_produ,lista_precios):
	lista_prod_posibles=imprimir_productos_posibles(dicc_produ)
	indice_prod_lista_posibles=validar_eleccion_producto(lista_prod_posibles,"el numero de producto",1)
	producto=lista_prod_posibles[int(indice_prod_lista_posibles)-1]
	sm=0
	while(True):
		print("El producto eleigido es: {}".format(producto))
		es_correcto=input("Es el producto deseado(s/n):")
		es_correcto=es_correcto.lower()
		if(es_correcto=="s"):
			break
		elif(es_correcto=="n"):
			indice_prod_lista_posibles=validar_eleccion_producto(lista_prod_posibles,"el numero de producto",1)
			producto=lista_prod_posibles[int(indice_prod_lista_posibles)-1]
	for i in range(len(dicc_produ)):
		if (producto==dicc_produ[str(i+1)]):
			indice_prod_dicc_produ=i
			break
	fecha=verificar_fecha(lista_precios,"")
	for x in range(len(lista_precios)):
		if (int(lista_precios[x][1])==indice_prod_dicc_produ):
			if(int(lista_precios[x][2])==fecha):
				if(int(lista_precios[x][0])==1):
					precio=float(lista_precios[x][3])
					sm=1
				elif(int(lista_precios[x][0])==2):
					precio=float(lista_precios[x][3])
					sm=2
				elif(int(lista_precios[x][0])==3):
					precio=float(lista_precios[x][3])
					sm=3
	if(sm==1):
		print("El mejor precio de {} lo tiene el supermercado Coto a {}$".format(producto,precio))
	elif(sm==2):
		print("El mejor precio de {} lo tiene el supermercado Jumbo a {}$".format(producto,precio))
	elif(sm==3):
		print("El mejor precio de {} lo tiene el supermercado Carrefour a {}$".format(producto,precio))
	else:
		print("error")
			
def pedir_fecha(momento):
	mes=input('Ingrese el numero del mes {} (ejemplo: 06):  '.format(momento))
	año=input('Ingrese el numero del año {} (ejemplo: 2015):  '.format(momento))
	return mes,año
	
def validar_fecha(momento):
	mes,año=pedir_fecha(momento)
	if len(mes)==1:
		mes='0'+mes
	while(not mes.isdigit or not año.isdigit or len(año)!=4 or len(mes)!=2):
		print('Los datos ingresados no son validos')
		mes,año=pedir_fecha(momento)
	return mes,año
	
def verificar_fecha(lista_precios,momento):
	mes,año=validar_fecha(momento)
	while True:
		periodo=año+mes
		for x in range (len(lista_precios)):
			if periodo in lista_precios[x][2]:
				return int(periodo)
		print('El periodo escogido no esta contemplado, elija uno de 2015/2016')
		mes,año=validar_fecha(momento)
		
#def validar_periodo():
	
		
def pedir_producto():
	return input('Ingrese el nombre del producto: ').lower()
	
def validar_producto(produ,estado):
	lista_productos_posibles=[]
	producto=pedir_producto()
	while True:
		for x in range (1,len(produ)+1):
			try:
				if(estado==0):
					if producto in produ[str(x)]:
						lista_productos_posibles.append(produ[str(x)])
				else:
					if producto in produ[x]:
						lista_productos_posibles.append(produ[x])
			except:
				continue
		if lista_productos_posibles!=[]:
			return lista_productos_posibles
		print('No se encontró ningún producto con nombre {} '.format(producto))
		producto=pedir_producto()
		
def imprimir_productos_posibles(dicc_produ):
	lista_productos_posibles=validar_producto(dicc_produ,0)
	for x in range(len(lista_productos_posibles)):
		print('{}. {}'.format(x+1,lista_productos_posibles[x]))
	return lista_productos_posibles
	
def validar_eleccion_producto(productos,mensaje,estado):
	indice_producto=pedir_eleccion(mensaje)
	if(estado==0):
		lista_productos=validar_producto(productos,1)
	else:
		lista_productos=productos
	while True:
		for numero in range(1,len(lista_productos)+1):
			if indice_producto!=str(numero):
				continue
			return indice_producto
		print('La opcion ingresada no es correcta')
		indice_producto=pedir_eleccion(mensaje)
	
def calcular_inflacion(precio_final,precio_inicial):
	return 100*((precio_final-precio_inicial)/precio_inicial)
	
def ciclo_eleccion(dicc_super,dicc_produ,lista_precios,opcion):
	if(opcion==INFLACION_POR_SUPERMERCADO):
			imprimir_inflacion_por_supermercado(dicc_super,dicc_produ,lista_precios)
	elif(opcion==INFLACION_POR_PRODUCTO):
			inflacion_por_producto(dicc_super,dicc_produ,lista_precios)
	elif(opcion==INFLACION_GENERAL_PROMEDIO):
			inflacion_general_promedio(dicc_super,dicc_produ,lista_precios)
	elif(opcion==MEJOR_PRECIO_PARA_UN_PRODUCTO):
			mejor_precio_para_un_producto(dicc_super,dicc_produ,lista_precios)
	elif(opcion==SALIR):
		print("Usted ha salido del sistema de analisis de precios...\nGracias por su visita ;)")
		return 0
	
def main():
	dicc_super=abrir_archivo(SUPERMERCADOS)
	lista_precios=abrir_archivo_precios(PRECIOS)
	dicc_produ=abrir_archivo(PRODUCTOS)
	while(True):
		mostrar_menu()
		opcion=validar_eleccion("la opcion")
		if(ciclo_eleccion(dicc_super,dicc_produ,lista_precios,opcion)==0):
			break
main()
