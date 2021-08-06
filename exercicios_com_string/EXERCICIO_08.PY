#Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.

def verificar_espaco(sentenca):
    for letra in sentenca:
        if letra == " ":
            return True
            break
    
def retirar_espaco(sentenca):
    palavras = sentenca.split()
    return "".join(palavras)

def inverter(sentenca):
    invertida = sentenca[::-1]
    return invertida

string = input("Digite algo para verificar se é um palíndromo: ")

# verificar se a frase tem espaço 

verif_espacos = verificar_espaco(string)

if verif_espacos == True:
    string_sem_espaco = retirar_espaco(string)
    string_invertida = inverter(string_sem_espaco)
    if string_invertida == string_sem_espaco:
        print("É um Palíndromo")
        print(f"{string} = {string[::-1]}")
    else:
        print("Não é um Palíndromo")
        print(f"{string} != {string[::-1]}")
else:
    string_invertida = inverter(string)
    if string_invertida == string:
        print("É um Palíndromo")
        print(f"{string} = {string[::-1]}")
    else:
        print("Não é um Palíndromo")
        print(f"{string} != {string[::-1]}")

