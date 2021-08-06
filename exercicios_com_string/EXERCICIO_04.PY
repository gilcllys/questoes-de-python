nome = input("Digite seu nome: ")
tamanho = len(nome)

for letra in range(1,tamanho+1):
    print(nome[:letra])