#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

from random import*

vetor = []
# crianda a o vetor de 5 numeros inteiros 
for valores in range(5):
    inteiro = randint(1,10)
    vetor.append(inteiro)

#soma dos valores
count = 0
for soma in range(len(vetor)):
    count = count + vetor[soma]
print(f"Soma total: {count} \n")

#multiplicação 
multiplicacao = 1
for mult in range(len(vetor)):
    multiplicacao = multiplicacao * vetor[mult]
print(f"Multiplicação total: {multiplicacao} \n")

# Todos os elementos
print(vetor,"\n")
