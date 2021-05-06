#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo
while True:
    print(80*'-*')
    num = float(input('Digite o valor :'))

    if num > 0 :
        print('o valor {} é POSITIVO'.format(num))
    elif num == 0:
        print(f'o valor {num} é neutro')
    else:
        print(f'o valor {num} é NEGATIVO')



