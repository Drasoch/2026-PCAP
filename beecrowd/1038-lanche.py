'''
Problema: beecrowd | 1038
Data: 2026.05.13
Estudante: Pedro André P. A. Blaka
'''
# Objetivo: calcular o valor a pagar dependendo do item e a quantidade escolhida

# --- ANÁLISE (LIAC) ---
# Entrada: duas entradas inteiras A = item esscolhido, B = quantidade
# Processamento: ler, e fazer o cálculo do total a pagar 
# Saída:  o total com duas casas decimais

A, B = input().split()
A = int(A)
B = int(B)

if A == 1:
    t = B * 4.00
elif A == 2:
    t = B * 4.50
elif A == 3:
    t = B * 5.00
elif A == 4:
    t = B * 2.00
elif A == 5:
    t = B * 1.50

print(f"Total: R$ {t:.2f}")
