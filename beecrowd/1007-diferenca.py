'''
Problema: beecrowd | 1007
Data: 2026.04.09
Estudante: Pedro André P. A. Blaka
'''
# Objetivo: ler quatro valores e descobrir a diferença do protuto de A e B pelo de C e D 

# --- ANÁLISE (LIAC) ---
# Entrada: quatro valores inteiros 
# Processamento: calcular o que é pedido pela fórmula A * B - C * D 
# Saída: deve ser exibido " DIFERENCA = valor"

A = int(input())
B = int(input())
C = int(input())
D = int(input())

dif = A * B - C * D 

print(f"DIFERENCA = {dif}")