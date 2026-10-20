/*
* Disciplina: 2026-PCAP
* Projeto   : fliperama em c
* Autor     : Pedro André P. A. Blaka
* LIAC      : Menu com validação...


*/
#include <stdio.h>

#define DONO "Pedro Blaka"

void linha(){
    printf("------------------------------------------------------------------------------------------------------------------\n");
}

void titulo(char texto[]){
    linha();
    printf("        %s\n", texto);
    linha();
}

int ler_numero(char mensagem[], int minimo, int maximo){
    int numero, lidos;

    printf("%s: ", mensagem);
    lidos = scanf("%d", &numero);
    while(lidos != 1 || numero < minimo || numero > maximo){
        if (lidos != 1){
            scanf("%*s");   /* joga fora o que não era numero */
        }
        printf("Opcao invalida! Tente de novo");
        lidos = scanf("%d", &numero);
    }
    return numero;
}

void mostrar_menu(){
    linha();
    printf("    Fliperama do %s\n", DONO);
    linha();
    printf("[1] Adivinhe o Numeron\n");
    printf("[2] Cadastrar Jogador\n");
    printf("[3] Listar jogadores \n");
    printf("[0] Sair\n");
    linha();
}

int main(){
    int opcao;

    mostrar_menu();
    opcao = ler_numero("Sua escolha", 0, 3);
    while(opcao != 0){
        if(opcao == 1){
            printf("O jogo entra na Fase 3.\n");
        }else if (opcao == 2){
            printf("O cadastro entra na Fase 2.\n");
        }else{
            printf("A lista entra na Fase 2.\n");
        }
        mostrar_menu();
        opcao = ler_numero("Sua escoha", 0, 3);
    }
    titulo("Ate a proxima!");
    return 0;
}