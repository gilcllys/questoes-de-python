#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit. 
c = float(input('temperatura em Celsius: '))
conversor = ( c* (9/5)) + 32 
print('sua temperatura é {} F'.format(conversor))