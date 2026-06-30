# ════════════════════════════════════════════════════════════
# Disciplina : Pensamento Computacional, Algoritmos e Programação (PCAP)
# Projeto    : Jogo "Par ou Ímpar"
# Arquivo    : par_impar.py
# Autor      : Pedro André Paes de Andrae Blaka
# Data       : 2026.06.25
# ════════════════════════════════════════════════════════════

import random

def vitoria(soma, num_jog):
    if soma % 2 == 0:
        soma = "par"
    else:
        soma = "impar"
    
    if num_jog == "par" and soma == "par":
        return "num_jog"
    if num_jog == "impar" and soma == "impar":
        return "num_jog"
    return "soma"

opcoes = ["par", "impar"]
pj = 0 
pm = 0 
for rodada in range(1, 6):
    print(f"--- Rodada: {rodada} ---")
    
    num_ma = random.randint(0, 5)
    jo = int(input("Seu Palpite (0 a 5): "))   #numero escolhido
    Pi = input("Sua jogada (par ou impar): ")  # jogada: (par e impar)
    num_jog = Pi.lower().strip()  
    soma = num_ma + jo

    if num_jog not in opcoes:
        print("Jogada inválida!")
        pm = pm + 1
    else:
        quem = vitoria(soma, num_jog)
        if quem == "num_jog":
            print("Você ganhou!")
            pj = pj + 1
        else:
            print("Você errou!")
            pm = pm + 1

print(f"Placar --> Você: {pj} | Máquina: {pm}")