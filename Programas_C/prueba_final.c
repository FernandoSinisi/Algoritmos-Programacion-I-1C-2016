#include<stdio.h>
#include<string.h>

void distancia(int longitud,int lista[]){
	for(int i=0;i<longitud-1;i++){
		int distancia=lista[i+1]-lista[i];
		printf("-%d-",distancia);
	}
}
	
int main (){
	int longitud=5;
	int lista[]={2,3,6,9,15};
	distancia(longitud,lista);
	return 0;
	}
