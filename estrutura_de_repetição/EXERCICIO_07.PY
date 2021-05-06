#Faça um programa que leia 5 números e informe o maior número. 
lista = []
for i in range(1,6):
     lista.append(i)

lista = sorted(lista,reverse=True)
print(lista)
print(f'{lista[0]} é o maior número')