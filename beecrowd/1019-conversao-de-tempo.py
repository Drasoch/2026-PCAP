'''
Problema: beecrowd | 1019
Data: 2026.04.09
Estudante: Pedro André P. A. Blaka
'''
# Objetivo: Ler uma duração inteira em segundos, coverter e exibir em horas:minutos:segundos

# --- ANÁLISE (LIAC) ---
# Entrada: um inteiro N  representando os segundos totais
# Processamento: extrair horas, minutos e segundos restantes por divisão inteira
# e módulo
# Saída: formato h:m:s sem zeros a esquerda - 0:9:16, não 00:09:16

N = int(input())

# // -> divisão inteira: retorna retorna o quociente INTEIRO da divisão sem pontos(virgulas)
# % -> módulo: retorna apenas o resto da divisão

# Quantas horas completas cabem em N segundos (1h = 3600 seg)
h = N // 3600

#segundos restantes após retirar as horas completas
N = N % 3600

# Quantos minutos completos cabem nos segundos restantes (1 min = 60 seg)
m = N // 60

# segundos que sobram após retirar os minutos completos
s = N % 60

# f-string monta o formato h:m:s -- sme zeros a esquerda
print(f"{h}:{m}:{s}")