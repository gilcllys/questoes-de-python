#Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def negativo_positivo(valor):
    if valor < 0:
        return "N"
    else:
        return "P"
print(negativo_positivo(-0.21))