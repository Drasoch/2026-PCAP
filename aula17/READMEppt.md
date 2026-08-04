# Variáveis: guardam algum valor ou texto

linha 37 --> opcoes = ["pedra", "papel", "tesoura", "lagarto", "spock"] na variável opcoes é guardado essas palavras que serão as suas opções de jogada
linha 38 --> pontos_jogador = 0 atribui o valor 0 a pontuação do jogador
linha 39 --> pontos_maquina = 0 atibui o valor 0 a pontuação da máquina

# Operadores: indicam qual operação será realizada

linha 50 --> pontos_maquina = pontos_maquina + 1 o operador + adiciona um ponto para a máquina em cima do valor que ja tinha sido  atribuido
linha 60 --> pontos_maquina = pontos_maquina + 1 mesma coisa do acima
linha 57 --> pontos_jogador = pontos_jogador + 1 igual os anteriores  mas aqui a pontuação é para o jogador

# Estrutura de repição: faz com que o código se repita até que uma condição seja atendida

linha 41 --> for rodada in range(1, 6): repete os comandos dentro dele até que a "rodada" chegue em 5

# Estrutura de condição: aplica uma condição a algo (se, se senão, senão)
linha 48 --> if...else... aqui é verificado se a sua jogada está entro as opções
linha 53 --> if...else... nessa estrutura é verificado de quem foi a vitória retornando um texto de vitória, empate, derrota
linha 13 --> if jogador == maquina: vrifica se a jogada do jogador é igual a da máquina e retorna empate

# Sub-rotina: atribui um comando a uma palavra que pode ser chamado a qualquer momento

linha 12 --> def resultado(jogador, maquina): define a "resultado" o resultado da partida vitória, empate ou derrota

# Entrada: você diz ao computador

# Saída: o que o computador te mostra