/*
* Disciplina    : 2026-PCAP
* Problema      : beecrowd 1178 
* Autor         : Pedro André P. A. Blaka
* Data          : 2026.10.06
* LIAC          : Ler um numero coloca-lo na primeira posição e as posiões subsequentes serão a metade da anterior, ate 99
*"N[i] = valor"
*/
#include <stdio.h>

int main(){
    float n[100];
    int i;
    scanf("%f", &n[0]);
    for (i = 1; i < 100; i++){
        n[i] = n [i - 1] / 2;
    }

    for (i = 0; i<100; i++){
        printf("N[%d] = %.4f\n", i, n[i]);
    }
    return 0;
}