#Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.

def converter(hora,minutos):
    tempo = []
    if hora > 12:
        hora_convertido = hora - 12
        tempo.append(hora_convertido)
        tempo.append(minutos)
    elif hora == 24:
        tempo.append(00)
        tempo.append(minutos)
    else:
        tempo.append(hora)
        tempo.append(minutos)
    return tempo


def saida (horas, tempo):
    if tempo == "A":
        print(f"""
        horário: {horas[0]}:{horas[1]} A.M.""")
    else:
        print(f"""
        horário: {horas[0]}:{horas[1]} P.M.""")

while True:
    while True:
        hora = int(input("Hora: "))
        if hora < 0 or hora > 23:
            print("!Entrada incorreta!")
            continue
        else:
            break
    while True:
        minutos = int(input("Minutos: "))       
        if minutos < 0 or minutos > 59:
            print("!Entrada incorreta!")
            continue 
    
        else:
            break
    while True:
        manha_tarde = input("Digite A (manhâ) ou P (tarde) : ")
        manha_tarde = manha_tarde.upper()
        if manha_tarde == "A" or manha_tarde =="P":
            break  
        else:
            print("!Entrada incorreta!")
            continue
    horario = converter(hora,minutos)
    saida(horario,manha_tarde)
    print("*"*45)