#Faça um programa que mostre os n termos da Série a seguir:
#  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
#Imprima no final a soma da série.

n = int(input(" Digite um número inteiro entre 1 e n: "))

superior = 1
inferior = 1
acumulador = 0
while (n >= superior):
    resto_divisão = inferior % 2
    if resto_divisão == 0:
        inferior = inferior + 1
    else:
        acumulador = acumulador + (superior / inferior)
        superior = superior + 1
        inferior = inferior + 1
print(acumulador)
    
