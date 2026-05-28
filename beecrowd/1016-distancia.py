'''
Problema: beecrowd | 1016
Data: 2026.04.23
Estudante: Pedro André P. A. Blaka
'''
# Objetivo: ler um valor e dizer quanto tempo leva para que o carro y se afaste essa distancia do carro x

# --- ANÁLISE (LIAC) ---
# Entrada: uma entrada inteira
# Processamento: fazer o calculo do tempo que o carro y leva para se afstar do carro x
# Saída: deve ser mostrado (O tempo) minutos

distancia = int(input())
tempo = distancia * 2  # *2 pois o carro y se afasta 2 km por minuto do carro x
print(f"{tempo} minutos")
