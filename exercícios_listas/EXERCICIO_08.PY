#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
import os
altura = []
idade = []

for dados in range(5):
    idade_pessoa = int(input("Digite a idade da pessoa: "))
    altura_pessoa = float(input("Digite a altura da pessoa: "))
    altura.append(altura_pessoa)
    idade.append(idade_pessoa)
    os.system("cls")

print(f"Alturas: {altura}")
print(f"Idades: {idade}")

altura.reverse()
idade.reverse()

print(f"Alturas inversas: {altura}")
print(f"Idades inversas: {idade}")