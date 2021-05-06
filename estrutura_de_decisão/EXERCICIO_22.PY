#Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão). 

valor = float(input('DIGITE UM VALOR PARA SABER SE É IMPAR OU PAR: '))

divisao = valor % 2 
if divisao == 0:
    print(f'{valor} é par ')
elif divisao != 0 :
    print(f'{valor} é impar ')
else:
    print('erro')
    