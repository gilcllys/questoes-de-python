#Faça um Programa que peça dois números e imprima o maior deles.
while True :
    print(50*'*-')
    n1 = float(input('número 1 :'))
    n2 = float(input('número 2 :'))

    if (n1 > n2) :
        print('{} é maior que {}'.format(n1,n2))
    elif (n2 > n1):
        print('{} é maior que {}'.format(n2,n1))
    else:
        print('eles são iguais') 
