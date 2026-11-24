# Fliperama em C++ (MeuApp v4.0)

## O que é:
é uma adaptação do fliperama em C já feito anteriormente, faz tudo igual e tem as mesmas funções 
(cadastrar, buscar, salvar e jogar adivinhe) além de também mostrar o menu bonitinho

## Como compilar e rodar:
g++ -Wall fliperama.cpp -o fliperama
./fliperama

## Arquivo:
- fliperama.cpp: o fliperma, com menu, e todas as funções funcionando
- jogadores.csv: onde é salvo apelidos (1° coluna) e quantidade de partidas (2° coluna)

## C x C++: o qeu mudou
| o que | no fliperama.c (linha) | No fliperama.cpp (linha) |
| --- | --- | --- |
| guardar um jogador | strcpy(apelidos[qtd], novo) (l.71) | apelidos.push_back(novo) (l.97) |
| comparar apelidos | strcmp(...) == 0 (l.53) | == (l.58) |
| a função que cadastra | int cadastrar(..., int qtd) (l.60) | void cadastrar(... &apelidos, ...) (l.87) |

## O que o C++ decidiu por mim
O C++ facilita a vida pois não precisa que eu defina algumas coisas como o tamanho do apelido, dos vetores e algumas outras coisas.
em C++ eu não preciso administrar :
A capacidade dos vectores, A memória de uma string (armazenamento do apelido)

## Autoavaliação:
| Critério | Conceito que espero | Onde se prova (arquivo e linha) |
| --- | --- | --- |
| 1. Estrutura, Compilação e Git | B | ao meu ver tudo foi compilado corretamente sem nenhum erro e passado para o github sem problemas |
| 2. Cadastro: vectors e referencia |C | O problema do cadastro duplo foi resolvido na linha 92 até a 95 e ao final uma outra possível solução (arquivo fliperama.cpp) |
| 3. Jogo e partidas | C | o jogo roda corretamente sem nenhum erro mostra as tentativas mas não guarda um histórico da partida mas contabiliza no arquivo |
| 4. Persistencia | B | no arquivo fliperama.cpp todos os resistos foram atendidos (eu acho) pois possui o salvar (funciona certinho) possui o jogadores.csv e os outors requisitos |
| 5. Documentação e comparação | C | N |