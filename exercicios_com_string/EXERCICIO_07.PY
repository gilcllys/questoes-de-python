#Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

# A-quantos espaços em branco existem na frase.
# B-quantas vezes aparecem as vogais a, e, i, o, u.

vogais = ["a","e","i","o","u"]

frase = input("Digite algo: ")

espaco = 0
vogal = 0

for letra in frase:
    if letra in vogais:
        vogal += 1
    elif letra == " ":
        espaco += 1
    else:
        continue

print(f"quantidade de vogais: {vogal} , quantidade de espaço: {espaco}")
        