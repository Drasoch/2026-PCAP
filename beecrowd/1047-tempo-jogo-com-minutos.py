'''
Problema: beecrowd |1047
Data: 2026.05.07
Estudante: Pedro André P. A. Blaka
'''
# Objetivo:calcular a duração do jogo atravéz da hora e minuto inicial e final

# --- ANÁLISE (LIAC) ---
# Entrada: 4 valores inteiros (hora e minuto inicial e final)
# Processamento: ler e fazer os cálculos necesários e comparar para atingir o objetivo
# Saída:  "O JOGO DUROU XX HORA(S) E YY MINUTO(S)"


hi, mi, hf, mf = map(int, input().split())

tim = (hi * 60) + mi   # tempo inicial em minutos
tfm = (hf * 60) + mf   # tempo final em minutos

# se o inicio é maior que o fim o jogo já passou da 00:00h
# nesse caso somamos 24h (24 * 60) à duração do jogo
if tim > tfm:
    ttm = (tfm - tim) + (24 * 60)
else:
    ttm = tfm - tim 

# Caso especial: inicio == fim -> o jogo dura 24h
# duração mínima 1min duração máxima 24h, então 0 vira 24h
if ttm == 0:
    ttm = 24 * 60

#ttm // 60 -> quantas horas cabem
#ttm % 60 -> minutos que sobraram
print(f"O JOGO DUROU {ttm // 60} HORA(S) E {ttm % 60} MINUTO(S)")

