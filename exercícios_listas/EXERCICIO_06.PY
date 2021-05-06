#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0
import os
codigos_alunos = []
media_alunos = []
# Lopp do aluno
for estudantes in range(1,11):
    codigo = int(input(f"Digite o código do aluno {estudantes} => "))
    codigos_alunos.append(codigo)
    notas_aluno = 0
    #loop para armazenamento das 4 notas 
    for avaliacao in range(1,5):
        aluno = float(input(f"Digite a nota {avaliacao} do aluno: "))
        notas_aluno = notas_aluno + aluno
    
    #comando para limpar todo o terminal
    os.system("cls")
    
    #calculo da média de cada aluno
    media = notas_aluno / 4
    media_alunos.append(media)

print("  RESULTADO FINAL")
#loop para filtrar as notas acima ou igual a 7
for notas_listas in range(len(media_alunos)):
    if media_alunos[notas_listas] >= 7:
        #Variável para rastrear o codigo do aluno referente a nota armazenada na lista
        codigo_rastreamento_nota = media_alunos.index(media_alunos[notas_listas])
        print(f"aluno (código:{codigos_alunos[codigo_rastreamento_nota]}) = {media_alunos[notas_listas]}")
