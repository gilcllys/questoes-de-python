#Faça um programa que calcule o mostre a média aritmética de N notas
print('Digite as notas ou 0 para encerrar o programa')
loop = True
media = 0
contador = 0
while loop:
    nota = float(input('Digite na nota: ')) 
    if nota != 0:
        media = media + nota 
        contador += 1
    else:
        break
total = media / contador

print(f'média total das notas = {total}')