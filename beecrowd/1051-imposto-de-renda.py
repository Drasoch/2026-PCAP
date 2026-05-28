'''
Problema: beecrowd | 1051
Data: 2026.05.14
Estudante: Pedro André P. A. Blaka
'''
# Objetivo: verificar a partir do salário de uma pessoa se e quanto ela precisa pagar de imposto

# --- ANÁLISE (LIAC) ---
# Entrada: uma entrada float (salário)
# Processamento: ler esse valor e verificar se a pessoa precisa e quanto precisa pagar de imposto
# Saída:  mostrar "Isento" caso n precise pagar imposto, caso precise mostrar o valor a pagar

S = float(input())
 

if S <= 2000:
    print("Isento")
elif 2000.00 < S and S <= 3000:
    S = (S - 2000) * 0.08
elif 3000.00 < S and S <= 4500:
    S = 1000 * 0.08 + (S - 3000) * 0.18
elif S > 4500:
    S = 1000 * 0.08 + 1500 * 0.18 + (S - 4500) * 0.28

print(f"R$ {S:.2f}")











