'''
Problema: beecrowd | NúmeroDoProblema
Data: ano.mes.dia
Estudante: Pedro André P. A. Blaka
'''
# Objetivo: Ler o número do funcionário, o número de horas trabalhadas, o valor que ele recebe por hora 
#e seu salário total

# --- ANÁLISE (LIAC) ---
# Entrada: 2 entradas de números intreiros e uma entrada de número decimal
# Processamento: calcular o valor total recebido atraves da multiplicação de V*H
# Saída: imprimir "NUMBER = (número do funcioário)"
#                 "SALARY = (valor recebido)"

# leitura das variáveis 
N =  int(input())
H =  int(input())
V = float(input())

#calculo do valor que ele receberá após as horas trabalhadas
SAL = V * H

print(f"NUMBER = {N}")
print(f"SALARY = U$ {SAL:.2f}")