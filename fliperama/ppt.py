# ==================================================
# Arquivo:    ppt.py (pasta fliperama)                          
# Conceitos: Jogo com módulo, lista como tabela de nomes, função com retorno, operador % para dar  volta
# Base: Jogo da Aula 17 (atividade 11)   
# Autor: Pedro André Paes de Andrade Blaka
# Data: 2026.08.11          
# ==================================================

#importa a função randint a bblioteca random, que sorteia um número inteiro aleatório em um intervalo definido
from random import randint

#importa as funções titulo e linha do arquivo telas.py
from telas import titulo, linha 

# importa a função ler_opcao que valida a entrada do usuário do arquivo modulos.py
from modulos import ler_opcao

# Pedra == 0, Papel == 1, Tesoura == 2
JOGADAS = ["PEDRA", "PAPEL", "TESOURA"]

def quem_vence(jogador, computador):
    if jogador == computador:
        return "empate"
    if jogador == (computador + 1) % 3:
        return "jogador"
    return "computador"

# mostra as opções de jogo
def mostrar_jogada():
    print("[0] Pedra")
    print("[1] Papel")
    print("[2] Tesoura")
    linha()


def jogar_ppt():
    titulo("PEDRA-PAPEL-TESOURA")

    pontos_jogador = 0
    pontos_computador = 0

    while pontos_jogador < 2 and pontos_computador< 2:
        mostrar_jogada()

        jogador = int(ler_opcao("Sua jogada", ["0", "1", "2"]))
        computador = randint(0, 2)

        print("Voce jogou " + JOGADAS[jogador] + ".")
        print("O PC jogou " + JOGADAS[computador] + ".")

        resultado = quem_vence(jogador, computador)

        if resultado == "empate":
            print("Empate! Ninguém pontua.")
        elif resultado == "jogador":
            pontos_jogador = pontos_jogador + 1
            print("Voce venceu a rodada")
        else:
            pontos_computador = pontos_computador + 1
            print("O PC venceu a rodada")

        print("Placar: voce:" + str(pontos_jogador) + " x " + str(pontos_computador) + " PC")

    if pontos_jogador > pontos_computador:
        titulo ("VOCE VENCEU A PARTIDA!!")
    else:
        titulo ("O PC VENCEU A PARTIDA!!")