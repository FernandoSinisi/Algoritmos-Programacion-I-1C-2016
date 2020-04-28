import math
def cal_hipotenusa(cateto_1,cateto_2):
	'''recibe los catetos, calcula y devuelve la hipotenusa de un triangulo rectangulo'''
	hipotenusa=math.sqrt((cateto_1**2)+(cateto_2**2))
	return hipotenusa

cal_hipotenusa(3,4)


