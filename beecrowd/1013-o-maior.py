'''
Problema: beecrowd | 1013
Data: 2026.05.14
Estudante: Pedro André P. A. Blaka
'''
# Objetivo: Ler três números e verificar qual dos 3 é maior

# --- ANÁLISE (LIAC) ---
# Entrada: três entradas inteiras que a pessoa irá escolher
# Processamento: ler e fazer os cálculos necessários para verificar o maior número 
# Saída: dado os três valores mostrar "X eh o maior"

A, B, C = input().split()   # separa as entradas por um espaço
A = int(A)
B = int(B)
C = int(C)
MAB = (A + B + abs(A - B)) / 2   #verifica o maior entre A e B 
MABC = int(MAB + C + abs(MAB - C)) / 2    #pega o resultado do anterior e verifica se é maior q C
print(f"{MABC:.0f} eh o maior")