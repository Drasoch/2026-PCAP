'''
Problema: beecrowd |1012
Data: 2026.04.23
Estudante: Pedro André P. A. Blaka
'''
# Objetivo: ler o valores e calcular as areas de algumas figuras geometricas

# --- ANÁLISE (LIAC) ---
# Entrada: tres entradas float A, B, C
# Processamento: fazer o calculo das areas a partir dos valores colocados
# Saída: mostrar no formato que é pedido as areas

A, B, C = input().split()  # separa os valores por espaço
A = float(A)
B = float(B)
C = float(C)
pi = 3.14159

# calculo das areas:
triangulo = (A * C) / 2 
circulo = pi * (C ** 2)
trapezio = ((A + B) * C ) / 2
quadrado = B ** 2
retangulo = A * B
print(f"TRIANGULO: {triangulo:.3f}")
print(f"CIRCULO: {circulo:.3f}")
print(f"TRAPEZIO: {trapezio:.3f}")
print(f"QUADRADO: {quadrado:.3f}")
print(f"RETANGULO: {retangulo:.3f}")