#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

print ("""
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% """)
taxa = float(input('qual o valor da sua hora de trabalho (salário/hora): '))
tempo = float(input('quanto tempo você trabalha por semana :'))
print(80*'-')
salario_bruto = taxa * tempo

if salario_bruto <= 900:
    fgts = salario_bruto * 0.11
    inss = salario_bruto * 0.10
    descontos = salario_bruto - inss
    salario_liquido = salario_bruto - descontos
    print(f"""
    salário Bruto:                          : R$ {salario_bruto}
        (-) IR (0%)                         : R$   ISENTO  
        (-) INSS ( 10%)                     : R$  {inss}
        FGTS (11%)                          : R$  {fgts}
        Total de descontos                  : R$  {descontos}
        Salário Liquido                     : R$  {salario_liquido} """)   

elif  900 < salario_bruto <= 1500:
    imposto_renda = salario_bruto *0.05
    fgts = salario_bruto * 0.11
    inss = salario_bruto * 0.10
    descontos = salario_bruto - inss - imposto_renda
    salario_liquido = salario_bruto - descontos
    print(f"""
    salário Bruto:                          : R$  {salario_bruto}
        (-) IR (5%)                         : R$  {imposto_renda}  
        (-) INSS ( 10%)                     : R$  {inss}
        FGTS (11%)                          : R$  {fgts}
        Total de descontos                  : R$  {descontos}
        Salário Liquido                     : R$  {salario_liquido} """)     

elif  1500 < salario_bruto <= 2500: 
    imposto_renda = salario_bruto *0.10
    fgts = salario_bruto * 0.11
    inss = salario_bruto * 0.10
    descontos = salario_bruto - inss - imposto_renda
    salario_liquido = salario_bruto - descontos
    print(f"""
    salário Bruto:                          : R$  {salario_bruto}
        (-) IR (10%)                         : R$  {imposto_renda}  
        (-) INSS ( 10%)                     : R$  {inss}
        FGTS (11%)                          : R$  {fgts}
        Total de descontos                  : R$  {descontos}
        Salário Liquido                     : R$  {salario_liquido} """)   

elif  salario_bruto >= 2500:
    imposto_renda = salario_bruto *0.20
    fgts = salario_bruto * 0.11
    inss = salario_bruto * 0.10
    descontos = salario_bruto - inss - imposto_renda
    salario_liquido = salario_bruto - descontos
    print(f"""
    salário Bruto:                          : R$  {salario_bruto}
        (-) IR (20%)                         : R$  {imposto_renda}  
        (-) INSS ( 10%)                     : R$  {inss}
        FGTS (11%)                          : R$  {fgts}
        Total de descontos                  : R$  {descontos}
        Salário Liquido                     : R$  {salario_liquido} """)  

