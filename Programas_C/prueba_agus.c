#include <stdio.h>
int main(){
	puts("Ingrese su nombre:");   //imprime como el prinf
	char nombre[20];
	scanf("%19s",nombre);               //esto %19s ya crea puntero  como char*
	int edad=0;
	printf("Ingrese su edad:");          //imprime el mensaje a mostrar
	scanf("%d",&edad);                // no te lo crea entonces lo pones q lo guarde en la posicion de edad 
	printf("hola %s tenes %d años",nombre,edad);
	return 0;
}
