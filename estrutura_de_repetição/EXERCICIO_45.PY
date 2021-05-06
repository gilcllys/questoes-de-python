#Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
# a-Maior e Menor Acerto;
# b-Total de Alunos que utilizaram o sistema;
# c-A Média das Notas da Turma.
#
# 
# Gabarito da Prova:

#01 - A
#02 - B
#03 - C
#04 - D
#05 - E
#06 - E
#07 - D
#08 - C
#09 - B
#10 - A
#Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.
import os
gabarito = ["A","B","C","D","E","E","D","C","B","A"]

notas_alunos = []
contador = 1
acertos = 0
aluno = 1
trava = True
while trava:
    print(" Para encerrar a prova digite 0")
    print(f"Aluno {aluno}")
    aluno = aluno + 1
    contador = 1
    acertos = 0 
    for i in range(len(gabarito)):
        resposta_aluno = input(f"""Resposta da questão {contador}:""")
        resposta_aluno = resposta_aluno.upper()
        contador = contador + 1 
        if resposta_aluno != "0":
            if resposta_aluno == gabarito [i]:
               acertos = acertos + 1
            else:
                continue
        else:
            trava = False
            break
    print("! Parabéns prova finalizada !")
    os.system("cls")
    notas_alunos.append(acertos)

print("""
************************************************************
                        NOTAS
************************************************************  """)
for i in range(len(notas_alunos)):
    print(f" Aluno {i+1} : {notas_alunos[i]}")
