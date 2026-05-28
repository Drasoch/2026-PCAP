'''
Problema: beecrowd | 1018
Data: 2026.05.01
Estudante: Pedro André P. A. Blaka
'''
# Objetivo: ler um valor inteiro e dcompô-lo em notas

# --- ANÁLISE (LIAC) ---
# Entrada: um valor inteiro positivo
# Processamento: ler, e fazer o cálculos para decompor o valor em notas
# Saída: uma lista em ordem decresente de notas

n = int(input())   #valor inteiro (dinheiro a ser decomposto)
print(f"{n}")

n100 = n // 100; n = n % 100  #pega o valor e divide por 100, o resto agora é n 
n50 = n // 50; n = n % 50     #pega n e divide por 50 n agr é o resto dessa divisão
n20 = n // 20; n = n % 20     #repete o processo nessa nota e nas demais até chegar na nota de 1
n10 = n // 10; n = n % 10
n05= n // 5; n = n % 5
n02 = n // 2; n = n % 2
n01 = n                       # o que sobrou de todas as divisões em notas de 1 real


print(f"{n100} nota(s) de R$ 100,00") 
print(f"{n50} nota(s) de R$ 50,00")
print(f"{n20} nota(s) de R$ 20,00")
print(f"{n10} nota(s) de R$ 10,00")
print(f"{n05} nota(s) de R$ 5,00")
print(f"{n02} nota(s) de R$ 2,00")
print(f"{n01} nota(s) de R$ 1,00")