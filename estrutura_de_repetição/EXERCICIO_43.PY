#O cardápio de uma lanchonete é o seguinte:
#Especificação   Código  Preço
#Cachorro Quente 100     R$ 1,20
#Bauru Simples   101     R$ 1,30
#Bauru com ovo   102     R$ 1,50
#Hambúrguer      103     R$ 1,20
#Cheeseburguer   104     R$ 1,30
#Refrigerante    105     R$ 1,00
#Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.

import os

lanches = {100: "Cachorro Quente", 101: "Bauru Simples", 102: "Bauru com ovo", 103: "Hambúguer", 104: "Cheeseburguer", 105: "Refrigerante"}
lista_qtd = []
lista_pedidos = []
lista_precos = []
cond = True
while cond:
    print("""
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00

Para encerrar o pedido digite zero no Código do pedido""")

    cod_pedido = int(input("Digite o código do pedido do cliente: "))
    qtd_pedido = int(input("Quantidade do pedido do cliente: "))
    #cachorro quente 
    if cod_pedido == 100:
        preco = qtd_pedido * 1.20
        
        lista_qtd.append(qtd_pedido)
        lista_pedidos.append(lanches[100])
        lista_precos.append(preco)
    #bauru simples
    elif cod_pedido == 101:
        preco = qtd_pedido * 1.30
        
        lista_qtd.append(qtd_pedido)
        lista_pedidos.append(lanches[101])
        lista_precos.append(preco)
    #bauru com ovo
    elif cod_pedido == 102:
        preco = qtd_pedido * 1.50
        
        lista_qtd.append(qtd_pedido)
        lista_pedidos.append(lanches[102])
        lista_precos.append(preco)
    #hamburguer 
    elif cod_pedido == 103:
        preco = qtd_pedido * 1.20

        lista_qtd.append(qtd_pedido)
        lista_pedidos.append(lanches[103])
        lista_precos.append(preco)
    #cheesebuguer
    elif cod_pedido == 104:
        preco = qtd_pedido * 1.30

        lista_qtd.append(qtd_pedido)
        lista_pedidos.append(lanches[104])
        lista_precos.append(preco)
    #refrigerante 
    elif cod_pedido == 105:
        preco = qtd_pedido * 1.00

        lista_qtd.append(qtd_pedido)
        lista_pedidos.append(lanches[105])
        lista_precos.append(preco)
    elif cod_pedido == 0:
        break
    os.system("cls")
print("""
**********************************************************************************************
*                                        CUPOM FISCAL                                        *
**********************************************************************************************""")

for i in range(len(lista_pedidos)):
    codigo_rastreamento = lista_pedidos.index(lista_pedidos[i])
    print(f"""
    QUANTIDADE: {lista_qtd[codigo_rastreamento]}          PEDIDO: {lista_pedidos[i]}          PRECO: R$ {round(lista_precos[codigo_rastreamento],2)}""") 
                                 
    print("")


total = sum(lista_precos)
print(f"""
***********************************************************************************************
TOTAL                                               R$ {round(total,2)}""")