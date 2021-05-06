#Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
from random import*
vetor_A = []
vetor_B = []
vetor_C = []
vetor_D = []

for position in range(10):
    #elementos do vetor A
    elemento_a = randint(1,10)
    vetor_A.append(elemento_a)

    #elementos do vetor B
    elemento_b = randint(1,10)
    vetor_B.append(elemento_b)

    #elementos do vetor C
    elemento_a = randint(1,10)
    vetor_C.append(elemento_a)

print(f"\nPrimeiro vetor: {vetor_A}")
print(f"Segundo vetor: {vetor_B}")
print(f"Segundo vetor: {vetor_C} \n")

for intercalados in range(len(vetor_A)):
    vetor_D.append(vetor_A[intercalados])
    vetor_D.append(vetor_B[intercalados])
    vetor_D.append(vetor_C[intercalados])
print(f"Terceiro vetor: {vetor_D}")