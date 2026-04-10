'''
Problema: beecrowd | 1006
Data: 2026.04.09
Estudante: Pedro André P. A. Blaka
'''
# Objetivo: ler tres valores de notas de umaluno e calcular a media ponderada delas

# --- ANÁLISE (LIAC) ---
# Entrada: tres valores float (as notas) a seres colocadas
# Processamento: calcular a media 
# Saída: print da média do aluno a partir de três notas 


A = float(input())
B = float(input())
C = float(input())


media = (A * 2 + B * 3 + C * 5) / 10

print(f"MEDIA = {media:.1f}")

