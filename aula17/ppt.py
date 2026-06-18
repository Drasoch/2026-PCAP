# ============================================
# Disciplina : Pensamento Computacional, algoritmos e Programação (PCAP)
# Projeto    : Jogo " Pedra-Papel-Tesoura"
# Arquivo    : ppt.py
# Autor      : Pedro André Paes de Andrae Blaka
# Data       : 2026.06.16
# ============================================

import random

#  === sub-rotina: vai devolver o texto conforme o resultado (uma rodada)
def resultado(jogador, maquina):
    if jogador == maquina:     # no primeiro return que for True o código encerra a função
         return "empate"
    if jogador == "pedra" and maquina == "tesoura":
        return "jogador"
    if jogador == "pedra" and maquina == "lagarto":
        return "jogador"
    if jogador == "papel" and maquina == "pedra":
        return "jogador"
    if jogador == "papel" and maquina == "spock":
        return "jogador"
    if jogador == "tesoura" and maquina == "papel":
        return "jogador"
    if jogador == "tesoura" and maquina == "lagarto":
        return "jogador"
    if jogador == "lagarto" and maquina == "papel":
        return "jogador"
    if jogador == "lagarto" and maquina == "spock":
        return "jogador"
    if jogador == "spock" and maquina == "tesoura" :
        return "jogador"
    if jogador == "spock" and maquina =="pedra":
        return "jogador"
    return "maquina"    # caso nenhum acima seja True a máquina venceu

opcoes = ["pedra", "papel", "tesoura", "lagarto", "spock"]
pontos_jogador = 0
pontos_maquina = 0

for rodada in range(1, 6):    # até 6 pois 6 é o limite e fica de fora
    print(f"--- Rodada {rodada} ---")
    jogada_maquina = random.choice(opcoes)
    #Leitura curta: ler + o lower() + .strip() em uma linha
    jogada_jogador = input("Sua jogada: ").lower().strip() # o .lower().strip() deixa tudo minusculo e sem espaço nas pontas


    if jogada_jogador not in opcoes:    # Caso a jogada não esteja nas opções
        print("❌ Jogada inválida! Você perde a rodada.")
        pontos_maquina = pontos_maquina + 1
    else:
        quem = resultado(jogada_jogador, jogada_maquina)   # caso as jogadas sejam iguais --> empate  (o elif faz essa verificação)
        if quem == "empate":
            print("🤝 Empate!")
        elif quem == "jogador":
            print("🎉 Você ganhou a rodada!")
            pontos_jogador = pontos_jogador + 1
        else:
            print("💀 A máquina ganhou a rodada!")
            pontos_maquina = pontos_maquina + 1

print(f"Placar final --> Você: {pontos_jogador} | Máquina: {pontos_maquina}")

'''
# ✊✋✌️ Pedra-Papel-Tesoura

Jogo de Pedra-Papel-Tesoura feito em Python na disciplina PCAP (Aula 17).
Você joga contra o computador em uma melhor de 5 rodadas, com placar.

# ▶️ Como jogar
1. Abra o terminal na pasta do jogo.
2. Rode: python ppt.py
3. A cada rodada, digite pedra, papel ou tesoura.
4. Ao fim das 5 rodadas, o programa mostra o placar final.

## ⚙️ Como funciona (resumo)
A cada rodada o computador sorteia uma jogada (random.choice) e lê a sua.
O texto digitado é limpo (.lower().strip()) e validado (in) antes de comparar.
Uma sub-rotina decide quem venceu e o programa soma os pontos das 5 rodadas.

## 🧠 O que eu pratiquei
- Strings e métodos de texto: .lower() e .strip() para limpar o que foi digitado
- Validação com in: aceitar só pedra, papel ou tesoura
- Comparação de textos (==): descobrir empate e vitórias
- random.choice: sortear a jogada da máquina
- Repetição (for): jogar as 5 rodadas e manter o placar
- Sub-rotinas (def/return): isolar a regra do jogo

## 🎯 Autoavaliação
Conceito pretendido: B

Justificativa (cite arquivo e linha de cada critério):
- O jogo funciona ............: ppt.py, linhas 09 a 62
- Trabalho com texto .........: ppt.py, linha __  (.lower().strip(), in, ==)
- Documentação e Git .........: este README + commits no GitHub
- Extensão/originalidade .....: ppt.py, linha __  (o que eu criei — nesse jogo eu implementei o Lagarto e o spock mas ainda sim poderia melhorar acrescntando algo mais,
 mas confio no julgamento do senhor)

Autor: Pedro André Paes de Andrade Blaka
'''