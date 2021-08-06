nome = input("Digite seu nome: ")
tamanho = len(nome)

for letra in range(tamanho):
    print(nome[:tamanho])
    tamanho -= 1 
