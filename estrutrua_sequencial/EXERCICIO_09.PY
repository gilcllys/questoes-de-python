#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
#C = (5 * (F-32) / 9). 
f = float(input('temperatura em Farenheit: '))
conversor = ((5 * (f-32)) / 9)
print('sua temperatura é {} °C'.format(conversor))
