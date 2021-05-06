#Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
#   $200 - $299
#   $300 - $399
#   $400 - $499
#   $500 - $599
#   $600 - $699
#   $700 - $799
#   $800 - $899
#   $900 - $999
#   $1000 em diante
#Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.

from random import*

def calculo_do_salario (vendas_brutas):
    vendas_brutas = randint(100,10000) 
    salario = 200 + (0.09*vendas_brutas)
    return round(salario,2)

salarios = [calculo_do_salario(i) for i in range(20)]

salarios_200_a_299 = [i for i in salarios if 200<=i<=299]
print(f"{len(salarios_200_a_299)} Vendedores receberam salários entre $200 - $299")


salarios_300_a_399 = [i for i in salarios if 300<=i<=399]
print(f"\n{len(salarios_300_a_399)} Vendedores receberam salários entre $300 - $399")


salarios_400_a_499 = [i for i in salarios if 400<=i<=499]
print(f"\n{len(salarios_400_a_499)} Vendedores receberam salários entre $400 - $499")


salarios_500_a_599 = [i for i in salarios if 500<=i<=599]
print(f"\n{len(salarios_500_a_599)} Vendedores receberam salários entre $500 - $599")


salarios_600_a_699 = [i for i in salarios if 600<=i<=699]
print(f"\n{len(salarios_600_a_699)} Vendedores receberam salários entre $600 - $699")


salarios_700_a_799 = [i for i in salarios if 700<=i<=799]
print(f"\n{len(salarios_700_a_799)} Vendedores receberam salários entre $700 - $799")


salarios_800_a_899 = [i for i in salarios if 800<=i<=899]
print(f"\n{len(salarios_800_a_899)} Vendedores receberam salários entre $800 - $899")


salarios_900_a_999 = [i for i in salarios if 900<=i<=999]
print(f"\n{len(salarios_900_a_999)} Vendedores receberam salários entre $900 - $999")


salarios_1000_a_mais = [i for i in salarios if i >= 1000]
print(f"\n{len(salarios_1000_a_mais)} Vendedores receberam salários entre $1000 - para cima")
