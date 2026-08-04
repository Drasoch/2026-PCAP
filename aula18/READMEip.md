# Variáveis: guardam algum valor ou texto

linha 24 --> opcoes = ["par", "impar"] aqui é guardado as suas opcoes de jogada
linha 25 --> pj = 0 aqui os é atribuído um valor numérico para sua pontuação
linha 26 --> pm = 0 mesma coisa do acima só que aqui são os pontos da máquina

# Operadores: indicam qual operação será realizada

linha 12 --> if soma % 2 == 0 o símbolo % realiza uma divisão e pega apenas o resto dela não o quociente
linha 35 --> soma  = num_ma + jo o símbolo + realiza a soma dos valores o atrbúi a variávl soma
linha 44 --> pj = pj + 1 aqui também é realizada a soma para aumentar a pontuação do jogador

# Estrutura de repição: faz com que o código se repita até que uma condição seja atendida

linha 28 -->  for rodada in range(1, 6) esse comando determina que enquanto a "rodada" não chegar em 5 o código se repetirá

# Estrutura de condição: aplica uma condição a algo (se, se senão, senão)

linha 12 a 21 --> if ... else..  aqui é verificado para ver se a condição estabelecida é atendida ou não gerando uma "conequência"  (2 if... else...)
linha 37 a 47 --> if... else... aqui a mesma coisa acontece mas no acima ele  verifica a vitória do jogador e retorna um resultado já nesse ele te dá o resultado e adiciona pontos para quem acertou

# Sub-rotina: atribui um comando a uma palavra que pode ser chamado a qualquer momento

linha 11 a 21 --> def vitoria(soma, num_jog): aqui é atribuido um código a palavra vitória e sempre que ela for usada você está chamando ese comando para ser executado

# Entrada: você diz ao computador
linha 32 -->  jo = int(input("Seu Palpite (0 a 5): ")) aqui a sua jogada (numérica) graças ao "int" é interpretado como um valor inteiro
linha 33 --> Pi = input("Sua jogada (par ou impar): ") sua jogada só que agora palavra (string) 

# Saída: o que o computador te mostra
linha 38 --> print("Jogada inválida!") caso a sua jogada (texto) não esteja nas opções o computador vai retornar essa mensagem
linha 43 --> print("Você ganhou!") caso você acerte e ganhe a rodada o computador vai retornar essa mensagem
linha 46 --> print("Você errou!") caso você erre e perca a rodada o computador vai retornar essa mensagem