'''
Problema: beecrowd | 1044
Data: 2026.04.16
Estudante: Pedro André P. A. Blaka
'''
# Objetivo: vericar se dois números interos são multiplos entre si

# --- ANÁLISE (LIAC) ---
# Entrada: Duas entradas interiras A e B na mesma linha separado por espaço
# Processamento: identificar maior e menor,  verificar se maior ´% menor == 0
# Saída: caso o numero seja multiplo retornara "Sao Multiplos"
#do contrário retornará "Nao sao Multiplos"

A, B = input().split()
A = int(A)
B =int(B)

#identifica maior e menor para aplicar o operador % corretamente
#(o resto deve ser calculado dividindo o maior pelo menor)
if A > B:
    maior = A
    menor = B
else:
    maior = B
    menor = A

# Operador módulo (%): retorna o resto da divisão inteira
# Se o resto for 0, o maoir é multiplo do menor -> são multiplos entre si.
if maior % menor == 0:     
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")