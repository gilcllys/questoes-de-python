#Altere o programa  anterior (EXERCICIO 04) permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação

populacao_A = float(input('Informe a número populacional A: '))
populacao_B = float(input('Informe a número populacional B: '))
taxa1 = float(input('taxa de crescimento populacional de A: '))
taxa2 = float(input('taxa de crescimento populacional de B: '))
contador = 0

while populacao_B >= populacao_A:
    contador += 1
    populacao_A = populacao_A*taxa1
    populacao_B = populacao_B*taxa2

print(f"""
Tempo : {contador} anos 
População A: {round(populacao_A)} habitantes 
Populção B: {round(populacao_B)} habitantes""")
