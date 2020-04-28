import math
def area_triangulo(base,altura):
	return base*altura/2

def calcular_resta(x1,y1,x2,y2):
	return (x1-x2,y1-y2)

def calcular_norma(x,y):
	return math.sqrt(x*x+y*y)

def calcular_distancia(x1,y1,x2,y2):
	p1,p2=calcular_resta(x1,y1,x2,y2)
	return calcular_norma(p1,p2)

def area_triangulo_lados(x1,y1,x2,y2,x3,y3):
	lado_A = calcular_distancia(x1,y1,x2,y2)
	lado_B = calcular_distancia(x1,y1,x3,y3)
	lado_C = calcular_distancia(x2,y2,x3,y3)
	semi_peri = (lado_A+lado_B+lado_C)/2
	return math.sqrt(semi_peri*((semi_peri-lado_A)*(semi_peri-lado_B)*(semi_peri-lado_C)))


