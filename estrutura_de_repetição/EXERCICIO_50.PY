# Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

n = int(input(" Números de termos N: "))

contador = 1
acumulador = 0
while (n >= contador):
    acumulador = acumulador + (1/contador)
    contador = contador + 1
print(acumulador)
