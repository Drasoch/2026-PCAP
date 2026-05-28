'''
Problema: beecrowd | 1021
Data: 2023.04.05
Estudante: Pedro André P. A. Blaka
'''
# Objetivo: ler um número e decompô-lo no menor número de notas e moedas possíveis

# --- ANÁLISE (LIAC) ---
# Entrada: um valor monetáio com duas casas decimais
# Processamento: fazer a decomposição  do valor em moeds e centavos
# Saída: lista formada na ordem do maior para o menor valor de notas e moedas

#divide os valores por . (n = notas, m = moedas)
n, m = input().split(".")

n = int(n) #define como iteiro para os calculos
m = int(m)

n100 = n //  100;     n = n %    100 # pega o valor divide por 100, n agora é o resto
n50 = n //    50;     n = n %     50   # respete o processo com 50 depois 25, 10 e assim por diante
n20 = n //    20;     n = n %     20
n10 = n //    10;     n = n %     10
n05 = n //     5;     n = n %      5
n02 = n //     2;     n = n %      2
n01 = n  #o que restou em notas de R$ 1.00

m50 = m //  50;   m = m %   50 #mesma lógica para as moedas 
m25 = m //  25;   m = m %   25
m10 = m //  10;   m = m %   10
m05 = m //   5;   m = m %    5
m01 = m  # o que restou em moedas de R$ 0.01



print("NOTAS:")
print(f"{n100} nota(s) de R$ 100.00")
print(f"{n50} nota(s) de R$ 50.00")
print(f"{n20} nota(s) de R$ 20.00")
print(f"{n10} nota(s) de R$ 10.00")
print(f"{n05} nota(s) de R$ 5.00")
print(f"{n02} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{n01} moeda(s) de R$ 1.00")
print(f"{m50} moeda(s) de R$ 0.50")
print(f"{m25} moeda(s) de R$ 0.25")
print(f"{m10} moeda(s) de R$ 0.10")
print(f"{m05} moeda(s) de R$ 0.05")
print(f"{m01} moeda(s) de R$ 0.01")
