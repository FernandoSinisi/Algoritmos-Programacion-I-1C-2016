def año_bisiesto(año):
	if año%4!=0:
		return False
	if año%100!=0:
		return True
	return (año%400==0)

def bisiesto(año):
	if año%4!=0:
		return False
	if año%100!=0:
		return True
	if año%400==0:
		return True
	return False

def es_bisiesto(año):
	if año%4==0:
		if año%100==0:
			if año%400==0:
				return True
			else:
				return False
		else:
			return True
	else:
		return False

	
def año_bisiesto_2(año):
	if año%4!=0:
		return False
	return año%100!=0 or año%400==0


def año_bisiesto_3(año):
	return año%4==0 and año%100!=0 or año%400==0
	
	






