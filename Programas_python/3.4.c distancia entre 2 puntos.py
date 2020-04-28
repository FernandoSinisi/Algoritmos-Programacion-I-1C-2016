import math

def calcular_distancia(x1,y1,x2,y2):
	p1,p2=calcular_resta(x1,y1,x2,y2)
	return calcular_norma(p1,p2)

def calcular_resta(x1,y1,x2,y2):
	return (x1-x2,y1-y2)

def calcular_norma(x,y):
	return math.sqrt(x*x+y*y)

calcular_distancia(5,7,2,3)

