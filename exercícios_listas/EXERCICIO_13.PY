#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

from random import*
# Listas de meses
meses_do_ano = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
#métodos gerador de temperaturas aleatórias 
def geradores_de_temperatura (temp):
    return round(uniform(25,40),2)
# aplicação da list comprehension para gerar temperaturas aleatórias
temperaturas = [geradores_de_temperatura(i) for i in range(1,13)]
#Média das temperaturas
media_das_temperaturas = sum(temperaturas)/len(temperaturas)
print(f"Média das temperaturas {round(media_das_temperaturas,2)}")
for cod_rastreamento_dos_meses, temp in enumerate(temperaturas):
    if temp > media_das_temperaturas:
        print(f"\nMês:{meses_do_ano[cod_rastreamento_dos_meses]} => Temperatura:{temp}ºC \n")
    else:
        continue
