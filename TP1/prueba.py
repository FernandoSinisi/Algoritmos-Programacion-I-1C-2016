a=2
b=0
def division():
	try:
		if a==2:
			return b
		numero=a/b
	except:
		print('quisiste dividir por cero')
		raise
	finally:
		print('chau')
division()
