#Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.
from random import*

def embaralhar (string):
    contador = 0
    verif_letra = []
    palavra_embaralhada = ""
    while len(string) > contador:
        cod_letra = randint(0,len(string)-1)
        if cod_letra not in verif_letra:
            verif_letra.append(cod_letra)
            contador += 1
            palavra_embaralhada += string[cod_letra]
        else:
            continue 
    print(palavra_embaralhada)  

palavra = input("Digite a palavra ao qual você gostaria de embaralhar: ")
embaralhar(palavra)