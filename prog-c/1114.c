/*
Problema 1114 BeeCrowd
2026.10.08
Pedro Anré Paes de Andrade Blaka
LIAC: Ler a senha digitada e verificar se é a senha correta 
caso nao seja "Senha Invalida", caso correta "Acesso Permitido"
*/

#include <stdio.h>

int main(){
    int senha;
    scanf("%d", &senha);

    while (senha != 2002) {
        printf("Senha Invalida\n");
        scanf("%d", &senha);
    }
    printf("Acesso Permitido\n");
    return 0;
}