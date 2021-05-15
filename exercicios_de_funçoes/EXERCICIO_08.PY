#Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado

def contador_de_digitos(num):
    numero = num
    VALOR = True
    contador = 0
    while VALOR:
        resto = num % 10
        resultado = num // 10
        num = resultado
        if resto != 0:
            contador += 1
        else:
            VALOR = False
    print(f"Digito: {numero} , Quantidade de dígitos: {contador}")

contador_de_digitos(4321)
    