#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento. 
valor =  float(input('digite o valor para saber se é decimal ou inteiro: '))

if valor == round(valor):
    print(f'{valor} é um valor inteiro')
else:
    print(f'{valor} é um valor decimal')