# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato. 
print("""Programa para ajudar na decisão de compra:
    orientações:
        1- Digite os valores dos preços 
        2- Espere o progrma fazer o calculo para ver a melhor opção""")
print(85*'-')
produto1 = float(input("preço 1: "))
produto2 = float(input("preço 2: "))
produto3 = float(input("preço 3: "))
precos = [produto1,produto2,produto3]
print(f'O melhor decisão de compra segundo a análise do nosso sistema : R$ {min(precos)}')

