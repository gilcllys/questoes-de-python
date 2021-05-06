#Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.

import os
import random
lista_de_valores = []
intervalo1 = []
intervalo2 = []
intervalo3 = []
intervalo4 = []
cont = True
while cont:
    print("Para encerrar o programa digite um valor negativo(ex.: -1)")
    valores = int(input("Digite valores entre 1 - 100: "))

    #intervalo 1 
    if valores >=0  and valores <=25:
        intervalo1.append(valores)
    #intervalo 2 
    elif valores >=26  and valores <=50:
        intervalo2.append(valores)
    #intervalo 3
    elif valores >=51  and valores <=75:
        intervalo3.append(valores)
    #intervalo 4
    elif valores >=76  and valores <=100:
        intervalo4.append(valores)
    elif valores < 0:
        cont = False
    os.system("cls")
print(f"""
Quantidade de valores no intervalo [0 - 25] : {len(intervalo1)}

Quantidade de valores no intervalo [26 - 50] : {len(intervalo2)}

Quantidade de valores no intervalo [51 - 75] : {len(intervalo3)}

Quantidade de valores no intervalo [76 - 100] : {len(intervalo4)} """)