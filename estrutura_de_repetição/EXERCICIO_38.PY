#Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:

#   A) Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
#   B) Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
#   C) A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário. 

salario_inicio = float(input("Informe a salário inicial: "))
data_incial = int(input("Informe a data de contrato: "))
data_final = int(input(" Informe a data de hoje: "))
taxa = 0.015
print(f'salário inicial = {salario_inicio}, Ano {data_incial}, taxa = 0 %')
print()
while data_incial <= data_final:
    salario_inicio = salario_inicio + salario_inicio*taxa
    data_incial = data_incial + 1
    print(f'salário = {round(salario_inicio,2)}, Ano = {data_incial} , taxa = {taxa*100} %')
    taxa = taxa*2

    
    
