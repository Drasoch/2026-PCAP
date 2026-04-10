'''
Problema: beecrowd | NúmeroDoProblema
Data: ano.mes.dia
Estudante: Pedro André P. A. Blaka
'''
# Objetivo: descrição sucinta do que o programa deve fazer

# --- ANÁLISE (LIAC) ---
# Entrada: quais dados o programa recebe e de que tipo?
# Processamento: ler, e verificar se o numero possui um mes correspondente ou nao
# Saída: deve ser mostrado o mes a qual o numero corresponde

M = int(input())     # cada numero corresponde a um mes 

if M == 1:
    print("January")
elif M == 2:
    print("February")
elif M == 3:
    print("March")
elif M == 4:
    print("April")
elif M == 5:
    print("May")
elif M == 6:
    print("June")
elif M == 7:
    print("July") 
elif M == 8:
    print("August")
elif M == 9:
    print("September")
elif M == 10:
    print("October")
elif M == 11:
    print("November")
elif M == 12:
    print("December")

'''
Caso o numero colocado seja maior que 12 (doze), por exemplo 14 (quatorze) dará erro pois
o exercicio não pediu para retornar nada como "esse mes nao existe" caso isso ocorresse
então ocorrerá so um erro
'''