#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
import os

vetor_all_values = []
vetor_par = []
vetor_impar = []

for position in range(20):
    valores = int(input("Digite os valores: "))
    vetor_all_values.append(valores)
    os.system("cls")

for valor in range(len(vetor_all_values)):
    resultado = vetor_all_values[valor] % 2
    if resultado == 0:
        vetor_par.append(vetor_all_values[valor])
    else:
        vetor_impar.append(vetor_all_values[valor])

print(f"""
lista completa: {vetor_all_values} 
lista par: {vetor_par}
lista ímpar: {vetor_impar} """)