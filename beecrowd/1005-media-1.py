'''
Problema: beecrowd | 1005
Data: 2026.04.09
Estudante: Pedro André P. A. Blaka
'''
# Objetivo: ler duas notas com pesos diferentes e calcular sua media ponderada

# --- ANÁLISE (LIAC) ---
# Entrada:duas entradas de float A e B 
# Processamento: calculo da média ponderada 
# Saída: exibir " MEDIA = valor" com cinco casas decimais
 
# xibe em casas decimais os valores 
A = float(input())
B = float(input())

#calculo da média ponderada peso da nota A = 3.5 peso da nota B = 7.5 soma = 11 
# divide-se por 11
media = (A * 3.5 + B * 7.5) / 11

print(f"MEDIA = {media:.5f}")