#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.

#    Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#    326 = 3 centenas, 2 dezenas e 6 unidades
#    12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16 

while True:
    num = input('digite o valor: ')

    if len(num) == 3:
        a = num[0]
        b = num[1]
        c = num[2]
        print(f'{num} = {a} centenas, {b} dezenas e {c}  unidades')
    elif len(num) == 2:
        a = num[0]
        b = num[1]
        print(f'{num} =  {a} dezenas e {b}  unidades')
    elif len(num) == 1:
        a = num[0]
        print(f'{num} =  {a} unidades')
    else :
        print('Valor incorreto')