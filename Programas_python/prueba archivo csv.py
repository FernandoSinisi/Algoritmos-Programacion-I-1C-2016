try:
	with open (ruta1,'r') as archivo1:
	     open (ruta2,'w') as archivo2:
	     csv1=csv.reader(archivo1)
	     csv2=csv.writer(archivo2)
	     dicc={}
	     for fruta,prec,cant in csv1:
			if not fruta in dicc:
				dicc[fruta]=[float(prec)*int(cant),int(cant)]
			else:
				dicc[fruta][0]+=float(prec)*int(cant)
				dicc[fruta][1]+=int(cant)
		for clave in dicc:
			csv2.writerow((clave,dicc[clave][0],dicc[clave][1]))
except IOError:
	print('mal pasada la ruta estupido')
except:
	

	 
