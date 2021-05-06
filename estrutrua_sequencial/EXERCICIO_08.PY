#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês
Valor = float(input('qual o seu salario por hora '))
hora = int(input('quanto vc trabalha no mes'))
salario = Valor * hora 
print('seu salário no mês é {}'.format(salario))
