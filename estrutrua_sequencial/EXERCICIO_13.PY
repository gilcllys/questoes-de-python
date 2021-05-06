#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7 
h = float(input('digite a sua altura :'))
homem = (72.7*h) - 58
mulher = (62.1*h) - 44.7 
print('altura {} metros , peso ideal : homens ({}) - mulheres({})'.format(h,homem,mulher))