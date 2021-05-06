#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

    #salário bruto.
    #quanto pagou ao INSS.
    #quanto pagou ao sindicato.
    #o salário líquido.
    #calcule os descontos e o salário líquido, conforme a tabela abaixo:

    #+ Salário Bruto : R$
    #- IR (11%) : R$
    #- INSS (8%) : R$
    #- Sindicato ( 5%) : R$
    #= Salário Liquido : R$

valor = float(input('qual o seu salario por hora: '))
hora = int(input('quanto vc trabalha no mês: '))
salario = valor * hora 

bruto = salario
ir = bruto *0.11
inss = bruto * 0.08
sind = bruto * 0.05
liquido = bruto - (ir + inss + sind)
print('+ Salário Bruto : R$ {}'.format(bruto))
print('- IR (11%) : R$ {}'.format(ir))
print('- INSS (8%) : R$ {}'.format(inss))
print('- Sindicato ( 5%) : R$ {}'.format(sind))
print('= Salário Liquido : R$ {}'.format(liquido))