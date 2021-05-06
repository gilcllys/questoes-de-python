#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles. 

valor1 = int(input('valor 1: '))
valor2 = int(input('valor 2: '))

for i in range(valor1+1, valor2):
    print(i)