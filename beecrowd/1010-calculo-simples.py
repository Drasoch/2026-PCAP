'''
Problema: beecrowd | 1010
Data: 2026.04.16
Estudante: Pedro André P. A. Blaka
'''
# Objetivo: ler o código, quantidade e valor unitario de duas peças e calcular o total a pagr

# --- ANÁLISE (LIAC) ---
# Entrada: duas linhas; cada uma com código int(), quantidade int()e valor unitario float()
# Processamento: fazer as contas necessárias para calcuar o total a pagar
# Saída: "VALOR A PAGAR: R$ ___" com duas casas decimais

#le a primeira linha e separa os valores pelo espaço
cod1, qtd1, val1 = input().split()

#converte a quantidade para inteiro e o valor unitário para float
qtd1 = int(qtd1)
val1 = float(val1)

# le a segunda linha e separa os valores pelo espaço
cod2, qtd2, val2 = input().split()

#converte a quantidade para inteiro e o valor unitário para float
qtd2 = int(qtd2)
val2 = float(val2)

# calcula o valor total: subtotal da peça 1 + subtotal da peça 2.
total = (qtd1 * val1) + (qtd2 * val2)

print(f"VALOR A PAGAR: R$ {total:.2f}")