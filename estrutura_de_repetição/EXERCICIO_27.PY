#Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos. 
acumulador = 0
turmas_certas = []
turmas_incorretas = []
quantidade_turmas = []
turmas = int(input("Número de turmas total: "))
for i in range(1,turmas+1):
    quantidade_turmas.append(i)
    alunos_turma = int(input(f'Quantidade de alunos da turma {i} :'))
    if alunos_turma <= 40:
        quatidade_alunos = alunos_turma
        acumulador = acumulador + alunos_turma
        turmas_certas.append(quatidade_alunos)
    else:
        turmas_incorretas.append(alunos_turma)
print()
print()
print(60*'-')
print("""***Número de alunos por turma***""")
for m in range (len(turmas_certas)):
    print(f"""Turma {quantidade_turmas[m]} : {turmas_certas[m]}""")
media = acumulador/len(turmas_certas)
print(f'Média :{media} alunos/turma')

print()
print(60*'-')
print("""***Turmas com excedentes de alunos***""")
for m in range (len(turmas_incorretas)):
    print(f"""Turma {quantidade_turmas[m]} : {turmas_incorretas[m]}""")

