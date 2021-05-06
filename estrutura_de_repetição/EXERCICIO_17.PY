#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120 
fatorial = int(input(' Valor para calcular o faotrial: '))

print('resposta com While')
contador = 1
resultado = 1
while contador <= fatorial:
    resultado = resultado * contador
    print(contador)
    contador  = contador + 1    
print(resultado)


acumulador = 1
print('repostas com FOR')
for i in range (1,fatorial+1):
    acumulador *= i
    print(acumulador)
print(acumulador)