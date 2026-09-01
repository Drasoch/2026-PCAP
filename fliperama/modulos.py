# ==================================================
# Arquivo:    modulos.py                            
# Disciplina: 2026-PCAP                             
# Aula:       20                                    
# Autor:      Pedro André Paes de Andrade Blaka     
# Data:       2026.08.04                            
# Conceitos:  []                                    
# ==================================================

def ler_opcao(mensagem, validas):
    resposta = input(mensagem + ": ").strip()
    while resposta not in validas:
        print("Opção inválida! Tente novamente.")
        resposta = input(mensagem + ": ").strip()
    return resposta

def ler_numero(mensagem, minimo, maximo):
    numeros = []
    for n in range(minimo, maximo + 1):
        numeros.append(str(n))
    return int(ler_opcao(mensagem, numeros))


def ler_texto(mensagem):
    # So devolve quando o texto não estiver vazio.
    resposta = input(mensagem + ": ").strip()
    while resposta == "":
        print("Não pode ficar em branco! Tente de novo.")
        resposta = input(mensagem + ": ").strip()
    return resposta                       