def pedir_nombre():
	return (input('Ingrese el nombre a buscar en la agenda - * para salir: '))

def verificar_telefono():
	while True:
		telefono=input('Ingrese el telefono: ')
		print('') 
		while True:
			pregunta=input('Es este el telefono que desea agendar - s/n: ').lower()
			if pregunta=='s':
				return telefono
			elif pregunta=='n':
				break
			else:
				print('ERROR, Ingrese s si desea cambiar el telefono, de lo contrario ingrese n')
				print('')
				continue
		continue
	
	
def main():
	print('         Bienvenido a la agenda interactiva')
	revisar_agenda()
	print('')
	print('Ha salido de el programa')	
		
def	revisar_agenda():
	agenda={}
	print('')
	while True:
		nombre=pedir_nombre()
		if nombre=='*':
			break
		elif nombre in agenda:
			print(nombre+' telefono: '+agenda[nombre])
			print('')
			while True:
				decision=input('Desea cambiar el telefono agendado s/n : ').lower()
				print('')
				if decision=='n':
					break
				elif decision=='s':
					nuevo_telefono=input('Ingrese el nuevo telefono de '+nombre+': ')
					agenda[nombre]=nuevo_telefono
					break
				else:
					print('ERROR, Ingrese s si desea cambiar el telefono, de lo contrario ingrese n')
					print('')
					continue
			continue
		else:
			print('Agendando a '+nombre)
			print('')
			telefono=verificar_telefono()
			agenda[nombre]=telefono
			print('Telefono Agendado')
			
			
main()		 
				
			
				
				
	
