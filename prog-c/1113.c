/*
Problema 1113 BeeCrowd
2026.10.08
Pedro Anré Paes de Andrade Blaka
*/

#include <stdio.h>

int main(){
    int x, y;
    scanf("%d %d", &x, &y);
    while(x != y){
        if (x < y){
            printf("Crescente\n");
        }else{
            printf("Decrescente\n");
        }
        scanf("%d %d", &x, &y);
    }
    
    return 0;
}
