import math

def calcular_norma(x,y):
	return math.sqrt(x*x+y*y)

def v_normalizado(x,y):
	norma=calcular_norma(x,y)
	return x/norma,y/norma

v_normalizado(3,4)


