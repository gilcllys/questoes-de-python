#Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elega

import os


def desenhar_retangulo (linhas, colunas):
    sinais = ["+" , "−" , "|" ]
    forma = int(input(
"""
    Como gostaria de desenhar o seu retângulo:
    (0) +
    (1) −
    (2) |
    
    Digite o código do símbolo para selecionar: """))

    #linha do topo
    for c in range(colunas):
        print(sinais[forma],end=" ")
    print("")
    #linhas do meio
    for l in range(linhas-2):
        print(sinais[forma],end=" ")
        #espaços da linha do meio
        for e in range(colunas-2):
            print(" ",end=" ")
        print(sinais[forma])
    #linha da base
    for c in range(colunas):
        print(sinais[forma],end=" ")
    
    print("\n")

def loop():
    
    qtd_colunas = int(input("informe a largura do retângulo entre 1 a 20: "))
    while True:
        if 0 < qtd_colunas > 20:
            os.system("cls")
            print("valor incorreto, tente novamente")
            qtd_colunas = int(input("informe a largura do retângulo entre 1 a 20: "))
        else:
            print("\n")
            break
    qtd_linhas = int(input("informe a altura do retângulo entre 1 a 20: "))
    while True:
        if 0 < qtd_linhas > 20:
            os.system("cls")
            print("valor incorreto, tente novamente")
            qtd_linhas = int(input("informe a largura do retângulo entre 1 a 20: "))
        else:
            print("\n")
            break

    desenhar_retangulo(qtd_linhas,qtd_colunas)

def parar_ou_continuar():
    resposta = int(input("Digite 1 para continuar ou 0 para encerrar o programa: "))
    return resposta


# començando o programa

while True:
    loop()
    user = parar_ou_continuar()
    if user == 1:
        loop()
    else:
        print("""
        *********************************
        *!Obrigrado por usar o programa!*
        *********************************""")
        break
