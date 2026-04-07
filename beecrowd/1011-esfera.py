'''
Problema: beecrowd | 1011
Data: 2026.04.07
Estudante: Pedro André P. A. Blaka
'''
# Objetivo: ler o raido de uma esfera e calcular o volume dela com a fórmula (4/3) * pi * r**3
# --- ANÁLISE (LIAC) ---
# Entrada: um número decimal (o raio R)
# Processamento: será necessário calcular o volume da esfera com a fórmula
# Saída: mostrar na tela o formato "VOLUME = valor" com 3 casas decimais

# o float faz com que o número apareça em sua forma decimal (ponto flutuante)

R = float(input())

# atribuir o valor de pi como constante (não usar math.pi)

pi = 3.14159

#4.0/3 garante a divisão decimal - dica do enunciado
# R**3 -  ** = pontencia 

V = ( 4.0 / 3) * pi * R ** 3 

# :.Xf - Faz com q o número apareça com o número de casa decimais que você deseja  (X = incognita)

print(f"VOLUME = {V:.3f}")