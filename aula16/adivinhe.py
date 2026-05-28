# ======================================================================
# Discplina : Pensamento computacional, algoritmos e programação (PCAP)
# Projeto   : Jogo "Adivinhe o Número" 
# Arquivo   : adivinhe.py
# Autor     : Pedro André Paes de Andrade Blaka
# Data      : 28/05/2026
# ======================================================================

import random

# 1) sorteamos um número aleatório entre 1 e 10
numero_secreto = random.randint(1,10)

# 2) Pedimos um palpite (input devolve TEXTO; convertemos para inteiro)
palpite = int(input("Digite um número de 1 a 10: "))

# 3) Mostramos o resultado deste primeiro teste

