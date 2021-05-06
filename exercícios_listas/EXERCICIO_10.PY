#Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

from random import*
vetor_A = []
vetor_B = []
vetor_C = []

for position in range(10):
    #elementos do vetor A
    elemento_a = randint(1,10)
    vetor_A.append(elemento_a)

    #elementos do vetor B
    elemento_b = randint(1,10)
    vetor_B.append(elemento_b)

print(f"\nPrimeiro vetor: {vetor_A}")
print(f"Segundo vetor: {vetor_B} \n")

for intercalados in range(len(vetor_A)):
    vetor_C.append(vetor_A[intercalados])
    vetor_C.append(vetor_B[intercalados])
print(f"Terceiro vetor: {vetor_C}")
