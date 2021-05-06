#O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:

#    Lojas Tabajara 
#    Produto 1: R$ 2.20
#    Produto 2: R$ 5.80
#    Produto 3: R$ 0
#    Total: R$ 9.00
#    Dinheiro: R$ 20.00
#    Troco: R$ 11.00
#    ...
valores = []
somador = 0
identificador = []
acumulador = 0
while True:
    while True:
        precos = float(input('preço do produto :'))
        if precos != 0:
            valores.append(precos)
            somador += precos
            acumulador += 1
            identificador.append(acumulador)
        else:
            break
    print(f'total : {round(somador,2)}')

    dinheiro = float(input('valor pago pelo cliente: '))
    print()

    print(70*'-')
    print('Lojas Tabajaras')
    print(70*'-')

    for i in range(len(valores)):
        print(f"""Produto {identificador[i]} : R$ {valores[i]}""")

    troco = dinheiro - somador
    print(f'Total: R$ {somador}')
    print(f'Dinheiro: R$ {dinheiro}') 
    print(f'Troco: R$ {troco}')
    print()
    print(80*'*-')
