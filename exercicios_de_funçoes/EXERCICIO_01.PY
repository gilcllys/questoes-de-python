#Faça um programa para imprimir:
#    1
#    2   2
#    3   3   3
#    .....
#    n   n   n   n   n   n  ... n
#para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

def piramide ():
    count = 1
    n = int(input("Quantidade de linhas (n): "))
    for linha in range(n):
        for coluna in range(count):
            print(f"{count}",end=" ")
        print("")
        count += 1
        
piramide()