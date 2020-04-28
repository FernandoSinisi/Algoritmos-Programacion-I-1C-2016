#include<stdio.h>
#include<string.h>

int main (){
	int longitud=5;
	int lista[]={2,3,6,9,15};
	int distancia=0;
	for(int i=0;i<longitud-1;i++){
		distancia=lista[i+1]-lista[i];
		printf("-%d-",distancia);
	}
	return 0;
	}
		
		
	
	
	
