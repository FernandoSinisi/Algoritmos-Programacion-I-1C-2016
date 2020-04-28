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
	
	precio_ini_sup1,precio_fin_sup1=precio_ini_fin("1",lista_precios,indice_prod_dicc_produ,fecha_ini,fecha_fin)
	precio_ini_sup2,precio_fin_sup2=precio_ini_fin("2",lista_precios,indice_prod_dicc_produ,fecha_ini,fecha_fin)
	precio_ini_sup3,precio_fin_sup3=precio_ini_fin("3",lista_precios,indice_prod_dicc_produ,fecha_ini,fecha_fin)
	inflacion_sup1=calcular_inflacion(precio_fin_sup1,precio_ini_sup1)
	inflacion_sup2=calcular_inflacion(precio_fin_sup2,precio_ini_sup2)
	inflacion_sup3=calcular_inflacion(precio_fin_sup3,precio_ini_sup3)
	print("La inflacion de {} en el supermercado Coto fue: {:.3}%".format(producto,inflacion_sup1))
	print("La inflacion de {} en el supermercado Jumbo fue: {:.3}%".format(producto,inflacion_sup2))
	print("La inflacion de {} en el supermercado Carrefour fue: {:.3}%".format(producto,inflacion_sup3))
