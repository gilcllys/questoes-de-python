#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58 
altura = float(input('digite a sua altura  :'))
peso = (72.7*altura) - 58 
print('o peso ideia para uma pessoa com {} de altura é {} kg'.format(altura,peso))