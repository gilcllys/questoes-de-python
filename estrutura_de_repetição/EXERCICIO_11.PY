# Altere o programa anterior para mostrar no final a soma dos números. 

valor1 = int(input('valor 1: '))
valor2 = int(input('valor 2: '))
soma = 0
for i in range(valor1+1, valor2):
    soma = soma + i
print(f'somatória de todos os números do intervalo: {soma}')