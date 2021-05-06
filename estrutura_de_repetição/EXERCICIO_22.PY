#Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível. 
n = int(input('Verificar numeros primos até: '))
mult = 0
#vai testar os valores entre 2 até o valor digitado -1 , se nao tiver nenhum divisor é primo, pois os números 1 e ele mesmo estão fora desse intervalo
for count in range(2,n):
     if (n % count == 0):
         print('Múltiplo de',count)
         mult += 1
if mult == 0:
    print('É primo')
else:
    print(f'tem {mult} múltiplos acima de 2 e abaixo de {n}')
    