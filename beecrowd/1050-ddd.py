'''
Problema: beecrowd | 1050
Data: 2026.04.09
Estudante: Pedro André P. A. Blaka
'''
# Objetivo: ler um código DDD e informar de qual cidade ele pertence 

# --- ANÁLISE (LIAC) ---
# Entrada: um número inteiro representando o código DDD
# Processamento: comparar o DDD lido com cada código da tabela usnado if/elif/else
# Saída: nome da cidade correspondente, ou "DDD não cadastrado" se não encontrado

# faz com que o DDD seja definido como um inteiro
DDD = int(input())

# estrutura if/elif/else (se/senão se/senão): testa cada condição em sequência
# apenas o primeriro bloco verdadeiro é executado os demais são ignorados
if DDD == 61:
    print("Brasilia")
elif DDD == 71:
    print("Salvador")
elif DDD == 11:
    print("Sao Paulo")
elif DDD == 21:
    print("Rio de Janeiro")
elif DDD == 32:
    print("Juiz de Fora")
elif DDD == 19:
    print("Campinas")
elif DDD == 27:
    print("Vitoria")
elif DDD == 31:
    print("Belo Horizonte")
else:
    # Nenhuma condição acima foi verdadeira -> DDD não está na tabela
    print("DDD nao cadastrado") 