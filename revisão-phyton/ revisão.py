# Concerto 01: trecho do "Adivinhe o Número" (Aula 16)
#segredo = 7
#palpite = input("Digite um número de 1 a 10: ")
#if palpite == segredo:
#    print("Acertou!!")
#else:
#    print(f"Errou! O segredo era {segredo}")

# O erro presente acima se encontra na linha 4 onde o palpite é interpretado como uma string pois não há int antes

# Forma Correta do concerto 01:
print("=== Adivinhe o Numero ===")
segredo = 7
palpite = int(input("Digite um número de 1 a 10: "))
if palpite == segredo:
    print("Acertou!!")
else:
    print(f"Errou! O segredo era {segredo}")

# Concerto 02: checagem de idade

#idade = int(input("Sua idade: "))
#if idade = 18:
#    print("Você tem exatamente 18 anos!")
#else:
#    print("Você não tem 18 anos.")

# O erro está no "=" da linha 23 ali deveria ser "==" para fazer uma comparação e executar a estrutura de condição

# Fora correta do Concerto 02:
idade = int(input("Sua idade: "))
if idade == 18:
    print("Você tem exatamente 18 anos!")
else:
    print("Você não tem 18 anos.")

# Concerto 03: contagem de rodadas
#contador = 1
#while contador <= 5:
#    print(f"Rodada {contador}")
#print("Fim de jogo!")

# O erro está que ao final da rodada ele não aumentou o contador

# Forma correta do Concerto 03: 
contador = 1
while contador <= 5:
    print(f"Rodada {contador}")
    contador = contador + 1
print("Fim de jogo!")

# Concerto 04: trecho do pedra-papel-tesoura (Aula 17)
jogada = input("pedra, papel ou tesoura? ")
