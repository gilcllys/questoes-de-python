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