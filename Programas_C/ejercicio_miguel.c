#include <stdio.h>
int main(void){
	int n,fact=1;
	printf("ingresar numero a calcularle el factorial\n");
	scanf("%d",&n);
	for(int i=1;i<=n;i++){
		fact=fact*i;
		}
	printf("el factorial de %d es %d\n",n,fact);
	return 0;
	}
	



