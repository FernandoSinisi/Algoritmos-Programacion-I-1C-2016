#include<stdio.h>
int main(){
	printf("Ingrese un numero: ");
	int n=0;
	int cont=0;
	scanf("%d",&n);
	for (int i=0;i<=n;i++){
		printf(" ");
	}
	printf("*\n");
	for(int i=0;i<=n;i++){
		printf("*");
		}
	printf("\n");
	for (int i=n;i>=0;i--){
		for (cont=0;cont<=i;cont++){
		printf(" ");
	}
	printf("*\n");
	}
	return 0;
}
