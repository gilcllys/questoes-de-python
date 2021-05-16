#Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
import random
from typing import Container

def dado1 ():
    x = random.randint(1,6)
    return x
def dado2():
    y = random.randint(1,6)
    return y
def menu():
    print("(1) jogar o dado (0) encerrar o jogo", end=" ")
    jogar = int(input(""))
    return jogar

VALOR = True
TRAVA = True
while VALOR:
    respota = menu()
    if respota == 1:
        valor1  = dado1()
        valor2 =  dado2()
        resultado = valor1 + valor2
        if resultado == 7 or resultado == 11:
            print(f"Dado1: {valor1} , Dado2: {valor2}")
            print(f"Total da soma: {resultado}")
            print("NATURAL, Ganhou!!\n")
        elif resultado in [2,3,8,12]:
            print(f"Dado1: {valor1} , Dado2: {valor2}")
            print(f"Total da soma: {resultado}")
            print("CRAPS, Perdeu!!\n")
        elif resultado in [4, 5, 6, 8, 9 ,10]:
            PONTO = resultado
            print(f"Dado1: {valor1} , Dado2: {valor2}")
            print(f"Total da soma: {resultado}")
            print("Ponto, jogue o dado novamente\n")
            while TRAVA:
                respota = menu()
                if respota == 1:
                    valor1  = dado1()
                    valor2 =  dado2()
                    resultado2 = valor1 + valor2
                    if resultado2 == PONTO:
                        print(f"Dado1: {valor1} , Dado2: {valor2}")
                        print(f"Total da soma: {resultado2}")
                        print("Ganhou!!\n")
                        TRAVA = False
                    elif resultado2 == 7:
                        print(f"Dado1: {valor1} , Dado2: {valor2}")
                        print(f"Total da soma: {resultado2}")
                        print("Perdeu!!\n")
                        TRAVA = False
                    else:
                        continue
                else:
                    print("!!programa encerrado!!")
                    VALOR = False 
    else:
        print("!!programa encerrado!!")
        VALOR = False
