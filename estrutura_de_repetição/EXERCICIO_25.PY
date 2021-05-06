# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada. 


print('Digite as idades ou 0 para encerrar o programa')
loop = True
media = 0
contador = 0
while loop:
    idade = float(input('Digite a idade: ')) 
    if idade != 0:
        media = media + idade 
        contador += 1
    else:
        break

total = media / contador

if 0 < total <= 25:
    print(f" media da turma: {total} (jovem)")

elif 26 <= total <= 60:
     print(f" media da turma: {total} (adulta)")

elif total > 60: 
    print(f" media da turma: {total} (idosa)")

