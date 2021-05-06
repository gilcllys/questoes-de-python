#Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.

from random import*

# função para gerar valores aleatórios de dados
def dados ():
    resultado = randint(1,6)
    return resultado
valores_dados = []

count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
count_5 = 0
count_6 = 0

# loop para jogar o dado 100 vezes
for i in range(100):
    valores = dados()
    if valores == 1:
        count_1 += 1
    elif valores == 2:
        count_2 += 1
    elif valores == 3:
        count_3 += 1
    elif valores == 4:
        count_4 += 1
    elif valores == 5:
        count_5 += 1
    elif valores == 6:
        count_6 += 1
    valores_dados.append(valores)
print(valores_dados)

print(f"""
Quantidade de vezes que cada valor aparece:
lado 1: {count_1}
lado 2: {count_2}
lado 3: {count_3}
lado 4: {count_4}
lado 5: {count_5}
lado 6: {count_6}
""")