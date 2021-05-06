#Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
#1 , 2, 3, 4  - Votos para os respectivos candidatos 
#(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
#5 - Voto Nulo
#6 - Voto em Branco
#Faça um programa que calcule e mostre:
#O total de votos para cada candidato;
#O total de votos nulos;
#O total de votos em branco;
#A percentagem de votos nulos sobre o total de votos;
#A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.
import os
def menu ():
    print("""
    ********************************************
        Bem vindo as eleições Presidenciais
    ********************************************
    CANDIDATOS:
    (1) Candidato 1         (N) Nulo
    (2) Candidato 2         (B) Branco
    (3) Candidato 3
    (4) Candidato 4
    

    (0) encerrar as votações
    
    obs: Digite o codigos referente a sua opção de voto 
    """)
    print()

candidato1 = []
candidato2 = []
candidato3 = []
candidato4 = []
branco = []
nulo = []
total = []

trava = True
#armazenamento dos votos
while trava:
    menu()
    voto = input("""Qual a sua de voto nas eleições 202X: """)

    voto = voto.lower()

    if voto  == "1":
        candidato1.append(voto)
        total.append(voto)
    elif voto == "2":
        candidato2.append(voto)
        total.append(voto)
    elif voto == "3":
        candidato3.append(voto)
        total.append(voto)
    elif voto == "4":
        candidato4.append(voto)
        total.append(voto)
    elif voto == "n":
        nulo.append(voto)
        total.append(voto)
    elif voto == "b":
        branco.append(voto)
        total.append(voto)
    elif voto == "0":
        trava = False
    os.system("cls")

#calculo dos votos 

porcentagem_cad1 = (len(candidato1)/len(total)) * 100
porcentagem_cad2 = (len(candidato2)/len(total)) * 100
porcentagem_cad3 = (len(candidato3)/len(total)) * 100
porcentagem_cad4 = (len(candidato4)/len(total)) * 100
porcentagem_n = (len(nulo)/len(total)) * 100
porcentagem_b = (len(branco)/len(total)) * 100

print(f"""
            RESULTADO DAS VOTAÇÕES 

Candidato 1 : {round(porcentagem_cad1,2)} %
Candidato 2 : {round(porcentagem_cad2,2)} %
Candidato 3 : {round(porcentagem_cad3,2)} %
Candidato 4 : {round(porcentagem_cad4,2)} %
Votos Nulos : {round(porcentagem_n,2)} %
Votos Brancos : {round(porcentagem_b,2)} %""")



