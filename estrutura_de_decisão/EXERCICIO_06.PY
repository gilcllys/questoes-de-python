#Faça um Programa que leia três números e mostre o maior deles. 


import random
valores = [random.uniform(0,10),random.uniform(0,10),random.uniform(0,10)]

print(valores)
print(f'O maior valor entre os três: {max(valores)}')