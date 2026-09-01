from modulos import ler_opcao, ler_numero
from telas import linha, titulo
from random import randint
# ==================================================
# Arquivo:    parimpar.py (pasta fliperama)                          
# Conceitos: 
# Base:  Jogo da Aula 18 
# Autor: Pedro André Paes de Andrade Blaka
# Data: 2026.09.01          
# ==================================================
def vencedor(soma, jog_j):
    if soma % 2 == 0:
        soma = "par"
    else:
        soma = "impar"

    if jog_j == "par" and soma == "par":
        return "jog_j"
    elif jog_j == "impar" and soma == "impar":
        return "jog_j"
    else:
        return "soma"


def jogar_poi():
    titulo("PAR ou IMPAR")
    linha()
    
    for rodada in range(1, 5):
        pm = 0
        pj = 0
        print("Rodada", rodada,":")
        num_jog = ler_numero("Escolha um número de 1 a 5", 1, 5)
        jog = ler_opcao("Sua Jogada par ou impar", ["par", "impar"])
        jog_j = jog.lower().strip
        num_comp = randint(1, 5)
        soma = num_jog + num_comp

        quem = vencedor(soma, jog_j)
        if quem == "jog_j":
            print("Você acertou!! Era", soma)
        if quem == "soma":
            print("Você errou!! Era", soma)

    
        
    print(f"Placar --> Você: {pj} | Máquina: {pm}")


