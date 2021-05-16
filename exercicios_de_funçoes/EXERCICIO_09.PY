#Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.#

def reversor (num):
    numero = num
    digitos = []
    VALOR = True
    while VALOR:
        resto = num % 10
        resultado = num // 10
        num = resultado
        if resto != 0:
            digitos.append(resto)
        else:
            VALOR = False
    print(f"{numero} --> ", end="")
    for valor in digitos:
        print(valor,end="")



reversor(98364)