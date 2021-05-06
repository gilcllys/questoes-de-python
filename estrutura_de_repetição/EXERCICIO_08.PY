#Faça um programa que leia 5 números e informe a soma e a média dos números. 

soma = 0
for i in range(1,6):
    valor = int(input('valor: '))
    soma = soma + valor
    
media = soma / i
print(f'média da somatório dos valores : {media}')