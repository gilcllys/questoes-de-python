#Faça um Programa que leia três números e mostre o maior e o menor deles. 


import random
valores = [random.uniform(0,10),random.uniform(0,10),random.uniform(0,10)]

print(valores)
print(f'O menor valor entre os três: {min(valores)}')