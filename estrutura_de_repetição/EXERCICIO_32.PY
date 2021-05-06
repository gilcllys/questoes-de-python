#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:

#    Fatorial de: 5
#    5! =  5 . 4 . 3 . 2 . 1 = 120

resultado = 1

valor = int(input("Valor para fatorar :"))
for i in range(1,valor+1):
    resultado = resultado * i
print()
print(70*'-')
print(f'Fatorial de: {valor}')    
print(f'{valor}! = ',end='')
for m in range (1,valor+1):
    print(f'{valor} .',end=' ')
    valor = valor - 1
print(f'= {resultado}')

