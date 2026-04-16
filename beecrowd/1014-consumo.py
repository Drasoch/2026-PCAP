'''
Problema: beecrowd | 1014
Data: 2026.04.16
Estudante: Pedro André P. A. Blaka
'''
# Objetivo: calcular o consumo médio de um veiculo em km/l

# --- ANÁLISE (LIAC) ---
# Entrada: uma entrada inteira em km e uma float litros
# Processamento: ler e fazer a média de consumo do carro
# Saída: deve aparecer o valor medio de consumo em km/l

# le a distancia percorrida em km 
X = int(input())

#le o total de combustível em decimal (float)
Y = float(input())

# calcula a média de consumo do carro
consumo = X / Y 

print(f"{consumo:.3f} km/l")