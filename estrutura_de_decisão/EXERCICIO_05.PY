#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    
#A mensagem "Reprovado", se a média for menor do que sete;
    
#A mensagem "Aprovado com Distinção", se a média for igual a dez. 
import random 
n1 = random.uniform(0,15)
n2 = random.uniform(0,15)

def media (x,y):
    med = (x + y)/2
    return med
resultado = media(n1,n2)

if resultado >=0 and resultado <= 10:
    if resultado == 10 :
        print(f'Aprovado com Distinção com média {resultado}')
    elif  resultado > 7:
        print(f'Aprovação com média {resultado}')
    else:    
        print(f'Reprovado com média {resultado} ')
else:
    print(f'nota {resultado} passou da média 10')
