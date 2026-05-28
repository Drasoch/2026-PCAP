'''
Problema: beecrowd | 1035
Data: 2026.04.23
Estudante: Pedro André P. A. Blaka
'''
# Objetivo: ler quatro valores e verificar se eles atemdem as condições definidas

# --- ANÁLISE (LIAC) ---
# Entrada: quatro entradas inteiras A, B, C e D
# Processamento: verificar se todas as conições verdadeiras e mostrar na tela uma mensagem correspondente
# Saída: caso eja verdadeiro: "Valores aceitos" caso contrário: "Valores nao aceitos"

A, B, C, D = input().split()

A = int(A)
B = int(B) 
C = int(C)
D = int(D)

if B > C and D > A and (C + D) > (A + B) and C > 0 and D > 0 and A % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
