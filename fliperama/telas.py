# ================================================
# Arquivo:    telas.py
# Disciplina: 2026-PCAP
# Aula:       20
# Autor:      Pedro André Paes de Andrade Blaka
# Data:       2026.08.04
# Conceitos:  []
# ================================================

# Definição  da Moldura: Caracteres e Tamanho
CAR = '-'
TAM = 60

# Função para desenhar uma linha na tela
def linha():
    print(CAR * TAM)

# função para desenhar um texto entre linhas
def titulo(texto):
    linha()
    print(texto.center(TAM))
    linha()
