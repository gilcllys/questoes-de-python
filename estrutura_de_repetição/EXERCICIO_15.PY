#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo. 
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
#    t1 t2 t3 
valores = int(input('quantos valores de fibonacci? '))
vetor = [0,1]
t1 = 0 
t2 = 1
if valores > 2 and valores != 0:
    while len(vetor) < valores:
        t3 = t1 + t2
        vetor.append(t3)
        t1 = t2
        t2 = t3
    print(vetor)
else: 
    print("ERRO")


