from math import exp
def conversor (valor):
    valores_convertidos = []
    for espaco in valor:
        espaco_convertido = int(espaco) * (0.000001)
        espaco_convertido = round(espaco_convertido,2)
        valores_convertidos.append(espaco_convertido)
    return valores_convertidos