#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1. 

numero_primo = int(input('Digite o valor: '))

valores = [1,2,3,4,5,6,7,8,9,numero_primo]

resto_zero = []
resto_nao_zero = []

for i in range(len(valores)):
    resposta = numero_primo % valores[i]
    if resposta == 0 :
        resto_zero.append(valores[i])
    else:
        resto_nao_zero.append(valores[i])

if len(resto_zero) == 2:
    print(f"""
    O valor {numero_primo} é primo""")
else:
    print(f"""
    O valor {numero_primo} não é primo""")


