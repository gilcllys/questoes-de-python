#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos). 
def tempo(velocidade,arquivo):
    temp = velocidade/arquivo
    return temp  
def conversor(segundos):
    conv = (segundos/60)
    return conv
    
vel = float(input("qual a velocidade :"))
tamanho = float(input("tamanho do arquivo: "))
convertido = conversor(tempo(vel,tamanho))
print ("O tempo total de donwload será {} minutos".format(convertido))