#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
import os
lista_notas = []
#armazenando as notas em uma lista
for notas in range(1,5):
    notas_alunos = float(input(f"NOTA DO ALUNO {notas}: "))
    os.system("cls")
    lista_notas.append(notas_alunos)
# imprimindo cada nota na tela por aluno 
contador = 1
for alunos in range(len(lista_notas)):
    print(f"Aluno {contador}: Nota = {lista_notas[alunos]}")
    contador = contador + 1

#media das notas
media = sum(lista_notas)/len(lista_notas)

print(f"Média das notas: {media}")

