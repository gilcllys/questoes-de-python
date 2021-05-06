#Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um. 
 
cd_total = int(input('Quantidade total de CDs :'))

acumulador = 0

for i in range(1,cd_total+1):
    cd_individual = float(input(f'preço do CD {i} :'))
    acumulador = acumulador + cd_individual

valor_medio = acumulador / cd_total
print()
print(f' valor médio : {round(valor_medio,2)} quantidade/preço ')

