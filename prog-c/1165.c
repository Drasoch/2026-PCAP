/*
* Disciplina    : 2026-PCAP
* Problema      : beecrowd 1175 
* Autor         : Pedro André P. A. Blaka
* Data          : 2026.10.06
* LIAC          : ler um valor interio maior que 1 e menor que 100 e verificar se é primo
*                   caso seja  "valor eh primo", caso não seja "valor nao eh primo"
*/

#include <stdio.h>

int main(){
    int casos, k, x;

    sacnf("%d", &casos);

    for (k = 0; k < casos; k++){
        scanf("%d", &x);
        if (eh_primo(x)){
            printf("%d eh primo\n", x);
        }else{
            printf("%d nao eh primo\n", x);
        }
    }

    return 0;
}

int eh_primo(int n){
    int i;

    if (n < 2){
        return 0;
    }
    for (i = 2; i * i <= n; i++){
        if (n % i == 0){
            return 0;
        }
    }
    return 1;
}
