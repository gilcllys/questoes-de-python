#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

from random import*
vetor = []
for position in range(10):
    elemento_a = randint(1,10)
    vetor.append(elemento_a)

somador = 0
for elemento in range(len(vetor)):
    somador = somador + (vetor[elemento])**2
print(somador)