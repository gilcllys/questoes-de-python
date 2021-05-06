#Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 


valor =  int(input('Possível número primmo :'))
contador = 0
# verificando quantos números divisores existem
for i in range(2,valor):
    divisao = valor % i
    if divisao == 0:
        contador = contador + 1
    else: 
        pass  
# conferindo se essa quantidade é indicador de um valor primo ou não
if contador > 0:
    for m in range(2,valor):
        divisao = valor % m
        if divisao == 0:
            print(f'{valor} é divisível por {m}')
        else: 
            pass  
else:
    print(f'{valor} é primo')