#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem
print()
print('resposta usando "while" ')
base = int(input('base: '))
expoente = int(input('expoente: '))
contador = 0
valor = 1
while contador <= expoente:
    valor *= base 
    contador += 1
print(f"""RESPOSTAS :
{base} ^ {expoente} = {valor}""")
