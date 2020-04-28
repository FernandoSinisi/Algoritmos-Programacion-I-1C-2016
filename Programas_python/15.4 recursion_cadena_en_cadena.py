def posiciones_de_cadena(cadena1,cadena2):
	cad1=cadena1.lower()
	cad2=cadena2.lower()
	return buscar_posiciones(cad1,cad2,0)
	
def buscar_posiciones(cadena1,cadena2,posicion):
	largocad1=len(cadena1)
	largocad2=len(cadena2)
	if cadena1=='' or largocad2>largocad1 or cadena2=='':
		return []
	if cadena1[:largocad2]==cadena2:
		return [posicion]+buscar_posiciones(cadena1[largocad2:],cadena2,posicion+largocad2)
	else:
		return buscar_posiciones(cadena1[1:],cadena2,posicion+1)
		
print(posiciones_de_cadena("Un tete a tete con Tete","te"))
	

	
