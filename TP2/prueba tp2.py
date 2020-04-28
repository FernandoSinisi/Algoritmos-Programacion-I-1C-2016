import csv
def abrir_archivo_4(ruta):
	with open (ruta) as archivo:
		archivo_csv=csv.reader(archivo)
		referencias=next(archivo_csv)
		for num,item,otro,algo in archivo_csv:
			print(num,item,otro,algo)
	#archivo.close()
			
def abrir_archivo(ruta):
	with open (ruta) as archivo:
		archivo_csv=csv.reader(archivo)
		referencias=next(archivo_csv)
		for num,item in archivo_csv:
			print(num,item)
	#archivo.close()
	
def main():
	abrir_archivo('/home/fs10/Escritorio/TP2/supermercados.csv')
	#abrir_archivo_4('precios.csv')
	#abrir_archivo('productos.csv')
	
main()

	
