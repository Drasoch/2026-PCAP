# mkdir --> cria uma pasta/diretório
# code --> cria um arquivo dentro do diretório (code revisão-phyton/ "nome do arquivo")
# Fundamentos da programação:
#    1. Variáveis e tipos de dados
#    2. Operadores
#    3. Entrada de dados
#    4. Saída de dados 
#    5. Estrutura de repetição
#    6. Estrutura de condição
#    7. Sub-rotinas

# 1. Variáveis e tipos e dados: guardam um dado para ser processado depois
#   str() --> o valor é interpretado como um texto 
input("qual seu nome: ") # o "seu nome será automaticamente interpretado como uma string"
#   int() --> o valor aqui é numérico inteiro 
int(input("qual sua idade: ")) # aqui é definido com o int que será uma entrada numérica inteira
#   float() --> o valor é interpretado como um decimal
float(input("qual sua altura: "))
# booleanos --> da a variável true ou false
Eu = True

# 2. Operadores: realizam alguma operação com os dados do código
#   Aritiméticos: 
#       + (soma: 1 + 1), - (subtração: 1 - 1), * (multiplicação: 1 * 2), / (divisão: 2 / 2)
#       ** (exponenciação: 2 ** 2), // (divisão inteira: 5 // 2 (vai retornar apemas o resultado inteiro)), % (Resto da divisão: 5 % 2 (retorna apenas o resto da divisão))
#   Comparação:
#       = (atribuição: num = 2), == (igualdade: 2 == 2), =! (diferença: 2 =! 3)
#       > (maior que: 3 > 2), >= (maior ou igual que: 2 >= 2), < (menor que: 2 < 3), <= (menor ou igual que: 2 <= 2)
#   Lógicos:
#       and (E: ambos valores tem que ser true), or (ou: apenas um tem que ser true), not (negação: ambos false)

# 3. Entrada de dados: o usuário fala ao computador
palavra = input("diga algo: ") # o input faz com que eu possa escrever para a máquina uma entrada

#4. Saída de dados: o que o computador me retorna
print(f"você disse: {palavra}") # o print retorna uma mensagem

# 5. Estrutura de repetição: repete um bloco de código por um tempo definido (for) ou até que uma condição seja atendida (while)
for num in range(5):  #vai repetir o número um 5 vezes
    print(1)

num = 0   #vai repetir menor ate que num seja menor que 10 e em baixo adiciono 1 para que não se repita infinitamente
while num <= 3: 
    print("menor")
    num = num + 1

# 6. Estrutura de condição: dependendo do resultado faz uma operação (if,elif,else)
num2 = int(input("digite um número: "))

if num2 % 2 == 0:
    print("par")
else:
    print("ímpar")
