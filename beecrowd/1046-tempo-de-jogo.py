'''
Problema: beecrowd | 1046
Data: 2026.05.07
Estudante: Pedro André P. A. Blaka
'''
# Objetivo: calcular o tempo de jogo após dado a hora inicial e final do jogo

# --- ANÁLISE (LIAC) ---
# Entrada: dois valores (hora inicial e hora final)
# Processamento: ler, calular para dar o tempo de jogo em horas
# Saída: "O JOGO DUROU XX HORA(S)"

A, B = input().split()
A = int(A)
B = int(B)

tim = (A * 60)    # transforma tudo em minutos
tfm = (B * 60)

if tim > tfm:
     ttm = (tfm - tim) + (24 * 60)  #faz as verificações para as contas
else:
    ttm = tfm - tim

if ttm == 0:      # Caso for igual a 0 o jogo completou 24h 
    ttm = 24 * 60


print(f"O JOGO DUROU {ttm // 60} HORA(S)")  #Decarta os "minutos" e deixa só as horas