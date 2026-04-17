'''
Problema: beecrowd | 1037
Data: 2026.04.16
Estudante: Pedro André P. A. Blaka
'''
# Objetivo: descrição sucinta do que o programa deve fazer

# --- ANÁLISE (LIAC) ---
# Entrada: quais dados o programa recebe e de que tipo?
# Processamento: ler, e verificar se o numero possui um mes correspondente ou nao
# Saída: deve ser mostrado o mes a qual o numero corresponde


valor = float(input())

#estruta if/elif/else: elif só é executado caso as afirmações anteriores forem falsas
# isso elimina a necessidade de ifs alinhado - código mais limpo e legível
if 0 <= valor <= 25:
    #colchete []indica que o extremo está incluido no intervalo
    print("Intervalo [0,25]")
elif 25 < valor <= 50:
    #parênteses () indica que o 25 não está incluido - apenas valores maiores  
    print("Intervalo (25,50]")
elif 50 < valor <= 75:
    print("Intervalo (50,75]")
elif 75 < valor <= 100:
    print("Intervalo (75,100]")
else:
    # nenhumas das condições anteriores foi verdadeira - número acima de 100 ou negativo
    print("Fora de intervalo")