/*
Problema 1073 BeeCrowd
2026.09.29
Pedro Anré Paes de Andrade Blaka
*/

#include <stdio.h>

int main(){
    int n, i;

    scanf("%d", &n);

    for (i = 2 ; i <= n; i = i + 2) {
        printf("%d^2 = %d\n", i, i * i);
    }

    return 0;
}