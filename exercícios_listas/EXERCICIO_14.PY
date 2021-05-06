#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#A-"Telefonou para a vítima?"
#B-"Esteve no local do crime?"
#C-"Mora perto da vítima?"
#"D-Devia para a vítima?"
#E-"Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

print("Responda s/n para as questões seguintes:\n")
#lista com todas as perguntas 
perguntas = [input("Telefonou para a vítima?\n"), input("Esteve no local do crime?\n"),input("Mora perto da vítima?\n"), input("Devia para a vítima?\n"), input("Já trabalhou com a vítima?\n")]

#lista armazenando todas as respotas
respostas = [i.lower() for i in perguntas]
#contagem de todas as respostas
contador = 0
for analise_das_respotas in respostas:
    if analise_das_respotas == "s":
        contador = contador + 1
    else:
        continue

#Analise das respotas
if contador == 2:
    print("\nSuspeita")
elif  contador == 3 or contador == 4:
    print("\nCúmplice")
elif contador == 5:
    print("\nAssassino")
else:
    print("\nInocente")
