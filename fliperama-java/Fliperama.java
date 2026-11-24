/*
* Disciplina : PCAP-2026
* Projeto    : MeuApp v5.0 - o Fliperama em Java (Aula 33)
* Autor      : Pedro André Paes de Andrade Blaka
* LIAC       : Menu do Fliperama em Java: metodos que desenham, um le
*              um numero dentr de uma faixa, e o laco que so para no 0 
*/
import java.util.Scanner;

public class Fliperama {
    static final String DONO = "Pedro Blaka";
    static Scanner teclado = new Scanner(System.in);

    static void linha(){
        System.out.println("=================================");
    }

    static void titulo(String texto) {
        linha();
        System.out.println("   " + texto);
        linha();
    }

    static int lerInteiro() {
        int numero = -1;

        if (teclado.hasNextInt()){
            numero = teclado.nextInt();
        }
        teclado.nextLine();
        return numero;
    }

    static int lerNumero(String mensagem, int minimo, int maximo){
        int numero;

        System.out.print(mensagem + ": ");
        numero = lerInteiro();
        while (numero < minimo || numero > maximo){
            System.out.print("Opcao invalida! Tente novamente: ");
            numero = lerInteiro();
        }
        return numero;
    }

    static void mostrarMenu(){
        linha();
        System.out.println("   FLIPERAMA DO " + DONO);
        linha();
        System.out.println("[1] Adivnhe o Numero");
        System.out.println("[2] Cadastrar jogador");
        System.out.println("[3] Listar jogadores");
        System.out.println("[0] Sair");
        linha();
    }

    public static void main(String[] args){
        int opcao;

        mostrarMenu();
        opcao = lerNumero("Sua escolha", 0, 3);
        while(opcao != 0){
            if (opcao == 1){
                System.out.println("O jogo entra na Fase 3");
            }else if (opcao == 2){
                System.out.println("O jogo entra Fase 2.");
            }else {
                System.out.println("A lista entra entra 2");
            }
            mostrarMenu();
            opcao = lerNumero("Sua escolha", 0, 3);
        }

        titulo("Ate a proxima!");
    }
}