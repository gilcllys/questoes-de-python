#Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

nome = input("Digite seu nome: ")
nome_upper = nome.upper()

def inverter (palavra):
    string = ""
    for i in palavra:
        string = i + string
    return string

palavra_invertida = inverter(nome_upper)

print()
print(f"Palavra original: {nome} -> {nome_upper} , palavra invertida: {palavra_invertida}")