#Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
#Os juros e a quantidade de parcelas seguem a tabela abaixo:
#Quantidade de Parcelas         % de Juros sobre o valor inicial da dívida
#   1                                  0
#   3                                  10
#   6                                  15
#   9                                  20
#   12                                 25
#Exemplo de saída do programa:
#Valor da Dívida    Valor dos Juros    Quantidade de Parcelas          Valor da Parcela
#R$ 1.000,00            0                       1                       R$  1.000,00
#R$ 1.100,00            100                     3                       R$    366,00
#R$ 1.150,00            150                     6                       R$    191,67
import os

lista_dividas = []
lista_valor_dos_juros = []
lista_qtd_de_parcelas = []
lista_valor_da_parcela = []

condicao =True
while condicao:
    divida = float(input("Qual o valor da dívida: "))
    qdt_parcelas = int(input("Quantas vezes gostaria de parcelar a dívida (1,3,6,9 ou 12): "))

    #quandidade de parcelas 
    # 1 PARCELA
    if qdt_parcelas == 1:
        porcentagem_juros = 0
        divida_altera = divida 
        valor_parcela = divida_altera/qdt_parcelas
        valor_juros = divida_altera - divida
        # acrescentando valores nas listas 
        lista_dividas.append(round(divida_altera,1))
        lista_valor_dos_juros.append(round(valor_juros,1))
        lista_qtd_de_parcelas.append(round(qdt_parcelas,1))
        lista_valor_da_parcela.append(round(valor_parcela,1))
    # 3 PARCELA
    elif qdt_parcelas == 3:
        porcentagem_juros = 1.10
        divida_altera = divida * porcentagem_juros
        valor_parcela = divida_altera/qdt_parcelas
        valor_juros = divida_altera - divida
        # acrescentando valores nas listas 
        lista_dividas.append(round(divida_altera,1))
        lista_valor_dos_juros.append(round(valor_juros,1))
        lista_qtd_de_parcelas.append(round(qdt_parcelas,1))
        lista_valor_da_parcela.append(round(valor_parcela,1))
    # 6 PARCELA
    elif qdt_parcelas == 6:
        porcentagem_juros = 1.15
        divida_altera = divida * porcentagem_juros
        valor_parcela = divida_altera/qdt_parcelas
        valor_juros = divida_altera - divida
        # acrescentando valores nas listas 
        lista_dividas.append(round(divida_altera,1))
        lista_valor_dos_juros.append(round(valor_juros,1))
        lista_qtd_de_parcelas.append(round(qdt_parcelas,1))
        lista_valor_da_parcela.append(round(valor_parcela,1))
    # 9 PARCELA
    elif qdt_parcelas == 9:
        porcentagem_juros = 1.20
        divida_altera = divida * porcentagem_juros
        valor_parcela = divida_altera/qdt_parcelas
        valor_juros = divida_altera - divida
        # acrescentando valores nas listas 
        lista_dividas.append(round(divida_altera,1))
        lista_valor_dos_juros.append(round(valor_juros,1))
        lista_qtd_de_parcelas.append(round(qdt_parcelas,1))
        lista_valor_da_parcela.append(round(valor_parcela,1))
    # 12 PARCELA
    elif qdt_parcelas == 12:
        porcentagem_juros = 1.25
        divida_altera = divida * porcentagem_juros
        valor_parcela = divida_altera/qdt_parcelas
        valor_juros = divida_altera - divida
        # acrescentando valores nas listas 
        lista_dividas.append(round(divida_altera,1))
        lista_valor_dos_juros.append(round(valor_juros,1))
        lista_qtd_de_parcelas.append(round(qdt_parcelas,1))
        lista_valor_da_parcela.append(round(valor_parcela,1))
    elif qdt_parcelas == 0:
        condicao = False
    os.system("cls")   
print(f"""
Valor da divida     valor juros      Qtd Parcelas   Valor da parcela""")
for i in range (len(lista_qtd_de_parcelas)):
    codigo = lista_dividas.index(lista_dividas[i])
    print(f"""         
R$ {lista_dividas[codigo]}                  {lista_valor_dos_juros[codigo]}               {lista_qtd_de_parcelas[codigo]}            R$ {lista_valor_da_parcela[codigo]}""")

