'''
Problema: beecrowd | 1017
Data: 2026.04.23
Estudante: Pedro André P. A. Blaka
'''
# Objetivo: calcular o quanto de combustível necessário para uma viagem baseado que o automóvel faz 12km/l

# --- ANÁLISE (LIAC) ---
# Entrada: dois valores inteiros (o tempo da viagem em horas e a velocidade média em km/h)
# Processamento: ler os valores e calcular o gasto de combustível
# Saída: deve ser mostrado o gasto de combustível em litros com tres casas decimais


# entradas:
# T = tempo gasto em horas
T = int(input())
# V = velocidade média em km/h
V = int(input())

# cálculo do gasto de combustível tempo * velocidade média / 12 ( a distancia que ele faz por litro)
G = (T * V) / 12
print(f"{G:.3f}")
