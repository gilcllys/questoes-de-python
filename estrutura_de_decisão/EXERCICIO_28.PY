#O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

#                         Até 5 Kg           Acima de 5 Kg
#    File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#    Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#    Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

#    Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar. 

def menu (escolha):
    escolha = eval(input("""
    Digite o código para escolher a carne desejada:
    (1) Filé duplo 
    (2) Alcatra 
    (3) Picanha 
    (4) Sair do programa
    
    Código aqui: """))
    while not  1<= escolha <=4:
        print()
        escolha = eval(input(' código 1 para Filé duplo \n código 2 para Alcatra \n Código 3 Picanha \n código 4 Sair do programa \n digite o código aqui:'));
    else:
        return escolha
def pagamento(opcao):
    opcao = eval(input(f"""
    Opções de pagamento:
    (1) Cartão de crédito tabajara
    (2) cartão de crédito, dinheiro ou cheque
    Digite sua opção:"""))
    if opcao == 1:
        return opcao
    else:
        return opcao
def file_duplo(peso):
    if  0 < peso <= 5:
        valor = peso * 4.90
        return valor
    elif peso > 5 :
        valor = peso * 5.80
        return valor
    else:
        print('VALOR INCORRETO, TENTE NOVAMENTE')
def alcatra(peso):
    if  0 < peso <= 5:
        valor = peso * 5.90
        return valor
    elif peso > 5 :
        valor = peso * 6.80
        return valor
    else:
        print('VALOR INCORRETO, TENTE NOVAMENTE')
def picanha(peso):
    if  0 < peso <= 5:
        valor = peso * 6.90
        return valor
    elif peso > 5 :
        valor = peso * 7.80
        return valor
    else:
        print('VALOR INCORRETO, TENTE NOVAMENTE')

loop = True
choice = menu(1)

while loop:
    if choice == 1:
        quantidade = float(input('Quantidade de Filé duplo desejado em Kg: '))
        forma_pagamento = pagamento(1)
        preco = file_duplo(quantidade)
        if forma_pagamento == 1:
            total = preco * 0.95
            print(f"""
            ----------------
            CUPOM FISCAL 
            ----------------
            TIPO DE CARNE : FILÉ DUPLO 
            PESO = {quantidade}
            PREÇO = R$ {round(total,2)}""")
            choice = menu(1)
        else:
            print(f"""
            ----------------
            CUPOM FISCAL 
            ----------------
            TIPO DE CARNE : FILÉ DUPLO 
            PESO = {quantidade}
            PREÇO = R$ {round(preco,2)}""")
            choice = menu(1)
            
    elif choice == 2:
        quantidade = float(input('Quantidade de Alcatra duplo desejado em Kg: '))
        forma_pagamento = pagamento(1)
        preco = alcatra(quantidade)
        if forma_pagamento == 1:
            total = preco * 0.95
            print(f"""
            ----------------
            CUPOM FISCAL 
            ----------------
            TIPO DE CARNE : ALCATRA 
            PESO = {quantidade}
            PREÇO = R$ {round(total,2)}""")
            choice = menu(1)
        else:
            print(f"""
            ----------------
            CUPOM FISCAL 
            ----------------
            TIPO DE CARNE : ALCATRA 
            PESO = {quantidade}
            PREÇO = R$ {round(preco,2)}""")
            choice = menu(1)
    elif choice == 3:
        quantidade = float(input('Quantidade de Picanha duplo desejado em Kg: '))
        forma_pagamento = pagamento(1)
        preco = picanha(quantidade)
        if forma_pagamento == 1:
            total = preco * 0.95
            print(f"""
            ----------------
            CUPOM FISCAL 
            ----------------
            TIPO DE CARNE : PICANHA 
            PESO = {quantidade}
            PREÇO = R$ {round(total,2)}""")
            choice = menu(1)
        else:
            print(f"""
            ----------------
            CUPOM FISCAL 
            ----------------
            TIPO DE CARNE : PICANHA
            PESO = {quantidade}
            PREÇO = R$ {round(preco,2)}""")
            choice = menu(1)
    elif choice ==4:
        loop = False
print('OBRIDADO POR USAR ESSE SISTEMA')


