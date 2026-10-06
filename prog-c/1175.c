/*
* Disciplina    : 2026-PCAP
* Problema      : beecrowd 1175 
* Autor         : Pedro André P. A. Blaka
* Data          : 2026.10.06
* LIAC          : ler 20 numeros em um vetor E trocar o ultimo valor digitado com a primira posição e assim por diante
*                   a saída será escrita "N[posição] = valor "
*/
#include <stdio.h>

int main(){
    int n[20], i;

    for(i = 0; i<20; i++){
        scanf("%d", &n[i]);
    }
    for(i = 0; i < 20; i++){
        printf("N[%d] = %d\n", i, n[19 - i]);
    }
    return 0;
}
