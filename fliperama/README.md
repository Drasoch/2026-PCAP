# Fliperama do Pedro Blaka

Um fliperama de terminal com três jogos, placar que não esquce e cadastro de jogadores. Projeto da disciplina PCAP, 1° ano Técnico em Informática do IFPR

## O que ele faz 

- Três jogos pelo menu: Adivinhe o Número, Pedra-Papel-Tesoura e Par ou Ímpar
- Placar que conta quantas vezes cada jogo foi jogado e continua contando depois 
de fehar o programa
- Cadastro de jogadores : cadastrar, listar, alterar e excluir

## Como rodar
```
cd fliperama
python3 main.py
```

## Os arquivos

- `main.py` - o gabinete: menu placar e chamadas
- `telas.py` - ferramentas visuais
- `modulos.py` - ferramentas de lógica: as três funções que perguntam e conferem
- `placar.py` - quantas partidas cada jogo teve
- `jogadores.py` - quem são os jogadores
- `adivinhe.py`, `ppt.py`, `parimpar.py` - um arquivo por jogo
- `placar.csv` e  `jogadores.csv` - os dados, que nascem sozinhos

a função `ler_texto` ficou no `modulos.py` porque ali estão localizados toas as ferramentas usadas nos jogos e isso facilita caso eu precise importar ela e mais uma função que está em modulos.py 

## De ond ele veio

- Aula 20: os três jogos viraram um programa só, módulos e menu
- Aula 21: entrou o Pedra-Papel-Tesoura e o placar passou a sobreviver
- Aula 22: entrou o cadastro de jogadores, com as quatro operações
- Aula 23: campo em branco barrado e o projeto documentado

## O que ainda nao funciona
- Nome com vírgula quebra a linha do arquivo, porque a  vírgula é o separador
- O apelido não pode ser um espaço em branco mas o nome sim 