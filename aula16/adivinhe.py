# ======================================================================
# Discplina : Pensamento computacional, algoritmos e programação (PCAP)
# Projeto   : Jogo "Adivinhe o Número" 
# Arquivo   : adivinhe.py
# Autor     : Pedro André Paes de Andrade Blaka
# Data      : 28/05/2026
# ======================================================================

import random
# === Sub-rotina: o jogo inteiro vira uma função reutilizável ===
def jogar(maximo, chances):
    numero_secreto = random.randint(1, maximo)
    acertou = False

    while chances > 0 and not acertou:
        palpite = int(input(f"Digite um número de (1 a " + str(maximo) +"): "))

        if palpite == numero_secreto:
            print(f"🎉 Acertou!")
            acertou = True
        elif palpite < numero_secreto:
            print(f"📈 Muito baixo!")
        else:
           print(f"📉 Muito alto!")
        chances = chances -1 
        print(f"Chances restantes {chances}")


    return acertou   # devolve True (venceu) ou False (perdeu)

# === Níveis guardados em uma lista de listas: [nome, maximo, chances] ===
niveis = [
    ["Muito Fácil", 10, 3],
    ["Fácil", 50, 5],
    ["Médio", 100, 6],
    ["Dificil", 500, 7],
    ["Impossivel", 1000, 10],
]
# == Menu de escolha do nível ==
print("Escolha o nível de dificuldade:")
print("1 - Muito Fácil (1 a 10, 3 chances)")
print("2 - Fácil       (1 a 50, 5 chances)")
print("3 - Médio       (1 a 100, 6 chances)")
print("4 - Difícil     (1 a 500, 7 chances)")
print("5 - Impossivel  (1 a 1000, 10 chances)")
opcao = int(input("Digite 1, 2, 3, 4 ou 5: "))

# A opcao 1 está na posição 0 da lista, por isso diminui 1 (opcao 1 = posição 0 a lista)
nivel = niveis[opcao - 1]

#  === Iniciamos o jogo com o nível escolhido ===
print(f"Você escolheu o nível: {[nivel[0]]}")
venceu = jogar(nivel[1], nivel[2])

if not venceu:
    print(f"💀 Fim de jogo! Tente um número mais fácil. 😉")