#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
import os
vetor_caracteres = []

for letras in range(10):
    caracteres = input("Digite uma letra do Alfabeto: ")
    vetor_caracteres.append(caracteres)
    os.system("cls")

for position in range(len(vetor_caracteres)):
    if vetor_caracteres[position] in "aeiou":
        continue
    else:
        print(vetor_caracteres[position],end=" ")
        