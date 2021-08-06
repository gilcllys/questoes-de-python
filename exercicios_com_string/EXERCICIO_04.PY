#Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

#F
#FU
#FUL
#FULA
#FULAN
#FULANO

nome = input("Digite seu nome: ")
tamanho = len(nome)

for letra in range(1,tamanho+1):
    print(nome[:letra])