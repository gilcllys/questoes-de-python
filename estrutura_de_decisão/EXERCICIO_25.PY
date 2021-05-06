#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

#    "Telefonou para a vítima?"
#    "Esteve no local do crime?"
#    "Mora perto da vítima?"
#    "Devia para a vítima?"
#    "Devia para a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente". 
while True:
    print(85*'-')
    print ('Esse programa irá descorbrir se você é culpado ou inocente em um crime, através das suas respostas. Responda sim ou não para as questões')
    print()
    pergunta1 = input('Telefonou para a vítima?')
    pergunta2 = input('Esteve no local do crime?')
    pergunta3 = input('Mora perto da vítima?')
    pergunta4 = input('Devia para a vítima?')
    pergunta5 = input('Devia para a vítima?')

    respostas = [pergunta1,pergunta2,pergunta3,pergunta4,pergunta5]
    sim = []
    nao = []

    for i in range(len(respostas)):
        if respostas[i] == "s" :
            sim.append(respostas[i])
        elif respostas[i] == 'n':
            nao.append(respostas[i])
    if len(sim) == 5:
        print()
        print(50*'*-')
        print('você é o ASSASSINO do crime')
        print(50*'*-')
    elif len(sim) == 3 or len(sim) == 4:
        print()
        print(50*'*-')
        print("você é CÚMPLICE do crime")
        print(50*'*-')
    elif len(sim) == 2:
        print()
        print(50*'*-')
        print('você é SUPEITO do crime')
        print(50*'*-')
    else: 
        print(50*'*-')
        print('você é INOCENTE')
        print(50*'*-')

