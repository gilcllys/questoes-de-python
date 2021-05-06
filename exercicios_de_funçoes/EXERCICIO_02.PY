#Faça um programa para imprimir:
#    1
#    1   2
#    1   2   3
#    .....
#    1   2   3   ...  n
#para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

def piramide ():
    count = 1
    n = int(input("Quantidade de linhas (n): "))
    for linha in range(n):
        counter = 1
        for coluna in range(count):
            print(f"{counter}",end=" ")
            counter += 1
        print("")
        count += 1
        
piramide()