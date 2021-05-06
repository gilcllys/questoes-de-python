#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. 

nota  =  float(input('digite um valor entre zero e 10: '))
loop = True
while loop: 
    if not 0<= nota <= 10:
        print(f'valor inválido, {nota} fora do intervalo')
        print()
        nota  =  float(input('digite um valor entre zero e 10: '))
        print(55*'-')
    else:
        loop = False
print(f'{nota} esta dentro do intervalo')
print('valor válido')

