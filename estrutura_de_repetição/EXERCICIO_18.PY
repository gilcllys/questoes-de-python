#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores

print('Digite os valores e para terminar o programa digite zero')
lista = []
while True:
    valores = float(input('Digite os valores: '))
    if valores != 0:
        lista.append(valores)
    else:
        break
print(f"""
Soma: {sum(lista)}
Maior valor : {max(lista)}
Menor valor : {min(lista)}""")
