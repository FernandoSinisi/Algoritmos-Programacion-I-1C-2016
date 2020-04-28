import math
def v_norma_resta(x1,y1,x2,y2):
	x,y=calcular_resta(x1,y1,x2,y2)
	return v_normalizado(x,y)

def calcular_norma(x,y):
	return math.sqrt(x*x+y*y)

def v_normalizado(x,y):
	norma=calcular_norma(x,y)
	return x/norma,y/norma

def calcular_resta(x1,y1,x2,y2):
	return (x1-x2,y1-y2)

v_norma_resta(7,5,3,2)


