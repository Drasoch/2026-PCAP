'''
Problema: beecrowd | 1009
Data: 2026.04.09
Estudante: Pedro André P. A. Blaka
'''
# Objetivo: Ler nome, salário fixo e total de vendas; calcular e exibir o total a receber

# --- ANÁLISE (LIAC) ---
# Entrada: nome (texto), salário fixo (float), total de vendas efetuadas (float)
# Processamento: comissão = vendas * 0.15 - total = salário fixo + comissão 
# Saída: exibir no formato exato "TOTAL = R$ valor" com duas casas decimais

#input() sem conversão - retorna como texto (str)
n = input()

#float(input()) - le valores numéricos (podem ser decimais)
s = float(input())  #salário fixo
v = float(input())  #total de vendas efetuadas no mês

#comissâo de 15% sobre o valor vendido
c = v * 0.15

#total a recber junto da comissão
st = s + c

# :.2f faz com que apareça duas casas decimais. dentro da f-string
print(f"TOTAL = R$ {st:.2f}")