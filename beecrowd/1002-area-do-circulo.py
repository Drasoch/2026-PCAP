'''
Problema: beecrowd | 1002
Data: 2026.04.07
Estudante: Pedro André P. A. Blaka
'''
# Objetivo: calcular  a area do circulo com a fórmula pi * r ** 2

# --- ANÁLISE (LIAC) ---
# Entrada: o programa recebe o valor R (que sera escolhido) e ele será float ou seja decimal como 10.00
# Processamento: precisa efetuar a conta da area do circulo
# Saída: deve aparecer na tela o resultado da area do circulo basado no seu raio

R = float(input())

pi = 3.14159

AREA = pi * R ** 2     # fórmula da area do circulo 

print(f"A={AREA:.4f}")