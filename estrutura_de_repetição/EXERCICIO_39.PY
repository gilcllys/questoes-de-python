#Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas. 

cod_aluno = []
altura_aluno = []
codigo = True
while codigo!=0:
    codigo = int(input('Informe o código do aluno: '))
    if codigo == 0:
        break
    else:
        altura = float(input('informe as alturas dos alunos: '))
        print(20*"-")
        cod_aluno.append(codigo)
        altura_aluno.append(altura)
aluno_alto = altura_aluno.index(max(altura_aluno))
aluno_baixo = altura_aluno.index(min(altura_aluno))
print(f"""
      Código do aluno mais alto: {cod_aluno[aluno_alto]}
      altura do aluno mais alto: {max(altura_aluno)}
      
      Código do aluno mais baixo: {cod_aluno[aluno_baixo]}
      altura do aluno mais baixo: {min(altura_aluno)}""")

