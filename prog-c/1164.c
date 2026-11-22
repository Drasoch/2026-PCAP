/*
Problema 1164 BeeCrowd
2026.10.08
Pedro Anré Paes de Andrade Blaka
LIAC: Leia N casos de teste. Para cada inteiro X, diga se X é perfeito
*/

#include <stdio.h>

int eh_perfeito(int, n){
    int i, soma = 0;

    for (i = 1; i < soma; i++){
        if (n % i == 0){
            soma = soma + i;
        }
    }
    return soma == n;
}

int main(){
    int casos, k, x;

    scanf("%d", &casos);
    for (k = 0; k < casos; k++){
        scanf("%d", &x);
        if(eh_perfeito(x))
    }
}