import random
def rata():
	camino=random.randrange(1,4)
	if camino==3:
		print('salio 7 minutos mas')
		return 7
	if camino==2:
		print('camino 2  sumo 5 min')
		return 5 + rata()
	print ('camino 1  sumo 3 min')
	return 3 + rata()

print(rata())
