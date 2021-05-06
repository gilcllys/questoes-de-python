#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

populacao_A = 80000
populacao_B = 200000

contador = 0

while populacao_B >= populacao_A:
    contador += 1
    populacao_A = populacao_A*1.03
    populacao_B = populacao_B*1.015

print(f"""
Tempo : {contador} anos 
População A: {round(populacao_A)} habitantes 
Populção B: {round(populacao_B)} habitantes""")
