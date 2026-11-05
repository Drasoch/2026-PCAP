# Fliperama em C (Meu app v3.0)

## O que é:
 Ele é uma adaptação do fliperama que ja tinha sido feito em python mas agora na linguagem C
mas agora ao envés de ter os três jogos foi feio apenas um o Adivinhe o Número, de resto é 
igual, cadastra e salva os apelidos dos jogadores.

## Como compilar e rodar:
gcc -Wall fliperama.c -o fliperma
./fliperama

# Arquivos:
fliperama.c: onde estão todos os códigos de comando para cadastrar, jogar, listar, etc.
jogadores.csv: a primeira coluna guarda o apelido dos jogadores, a segunda o número de 
partidas que eles jogaram

## Python x C: o que mudou
| O que | No jogadores.py (linha) | No fliperama.c (linha) |
|---|---|---|
| guardar um jogador | jogadores.append(novo) (l.28) | strcpy(apelidos[qtd], novo) (l.71) |
|comparar apelidos | == (l. 55/56) | strcmp(...) == 0 (l. 53/54)| 
| abrir sem arquivo | exists(ARQUIVO) (l. 114/127) | folpen == NULL (l. 129/140) |

## O que o C me obrigou a decidir:
sendo bem sincero eu não sei dizer mesmo lendo os dois arquivos de filperama (.py e .c) vou pensar nisso melhor

## Autoavaliação:
| Critério | Conceito que espero | Onde se prova |
|---|---|---|
| 1. Estrutura, compilação e Git | B | Tudo oq foi pedido está no devido lugar bem organizadp dentro do aquivo |
| 2.  Cadastro: menu, funções e vetores | B | o menu está correto e funcional, as funções todas funcionando conforme o que era para ser |
| 3. Jogo e partidas | B | o jogo roda normalmente e as partidas são registradas corretamente |
| 4. Persistencia | C | |
| 5. Documentção e comparação | C | |