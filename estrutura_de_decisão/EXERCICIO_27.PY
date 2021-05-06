#Uma fruteira está vendendo frutas com a seguinte tabela de preços:

#                         Até 5 Kg           Acima de 5 Kg
#    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#    Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

#   Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente. 

# função do menu principal
def fruta_escolhida (fruta):
    fruta = eval(input("""
    Digite o código para escolher a fruta desejada:
    (1) Maçã
    (2) Morango
    (3) comprar maçã e morango 
    (4) Sair do programa
    
    Código da fruta: """))
    while not  1<= fruta <=4:
        fruta = eval(input('Digite o código 1 para Maçã , 2 para Morango, 3 para comprar morango e maçã ou 4 Sair do programa'))
    else:
        return fruta
# função para calculo do preço de maçã 
def apple (peso):
    if  0 < peso <= 5: 
        preco = peso * 1.80
        return preco
    elif 5 < peso <= 8:
        preco = peso *1.50
        if preco > 25:
            novo_preco = preco *0.9
            return novo_preco
        else:
            return preco
    elif peso > 8:
        preco = (peso*1.5)*0.9
        return preco
# funcção par acalculo do preço de morango 
def morango (peso):
    if  0 < peso <= 5: 
        preco = peso * 2.50
        return preco
    elif 5 < peso <= 8:
        preco = peso * 2.20
        if preco > 25:
            novo_preco = preco *0.9
            return novo_preco
        else:
            return preco
    elif peso > 8:
        preco = (peso*2.20)*0.9
        return preco

# código começa aqui 
loop =True
choice = fruta_escolhida(1)
while loop:
    if choice == 1:
        fruta = float(input('Peso de maçã que deseja comprar (Kg) : '))
        escolha = apple(fruta)
        print(f"""
        MAÇÃ:
        - Quantidade : {fruta} Kg
        - Preço : R$ {round(escolha,2)}""")
        print(40*'*')
        choice = fruta_escolhida(1)
    elif choice == 2:
        fruta = float(input('Peso de Morango que deseja comprar (Kg) : '))
        escolha = morango(fruta)
        print(f"""
        MORANGO:
        - Quantidade : {fruta} Kg
        - Preço : R$ {round(escolha,2)}""")
        print(40*'*')
        choice = fruta_escolhida(1)
    elif choice == 3:
        fruta = float(input('Peso de maçã que deseja comprar (Kg) : '))
        fruta2 = float(input('Peso de Morango que deseja comprar (Kg) : '))
        escolha = apple(fruta)
        escolha2 = morango(fruta2)
        total = escolha + escolha2
        if total > 25:
            total_novo = total*0.90
            print(f"""
        MAÇÃ:
        - Quantidade : {fruta} Kg
        MORANGO:
        - Quantidade : {fruta2} Kg
        --------------------------
        PREÇO TOAL: R$ {round(total_novo,2)}""")
            print(40*'*')
            choice = fruta_escolhida(1)
        else:
            print(f"""
        MAÇÃ:
        - Quantidade : {fruta} Kg
        MORANGO:
        - Quantidade : {fruta2} Kg
        --------------------------
        PREÇO TOAL: R$ {round(total,2)}""")
            print(40*'*')
            choice = fruta_escolhida(1)
    elif choice == 4:
        loop = False
print('obrigado por usar o programa!')


