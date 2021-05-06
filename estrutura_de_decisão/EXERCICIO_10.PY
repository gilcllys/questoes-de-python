#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso. 
while True :
    turno_estudo = input("""Para receber a mensagem de acordo com seu turno escreva:
            M = Matutino
            V = Vespertino
            N = Noturno
        Depois aguarde sua mensagem!""")

    turno_estudo = turno_estudo.upper()
    if turno_estudo == "M":
        print('Bom Dia !')
    elif turno_estudo == 'V' :
        print('Boa Tarde !')
    elif turno_estudo == 'N' :
        print('Boa Noite !')
    else:
        print('VALOR INVÁLIDO')
