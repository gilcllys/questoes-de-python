#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

#    Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#    Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1. 

saque = int(input('Valor de saque: '))
if saque >= 10 and saque <= 600:
    #notas de 100
    notas100 = saque//100
    #resto de 100
    resto100 = saque % 100
    #notas de 50
    notas50 = resto100//50
    #resto de 50 
    resto50 = resto100 % 50
    #notas de 10
    notas10 = resto50 // 10
    #resto de 10
    resto10 = resto50 % 10
    #notas de 5
    notas5 = resto10 // 5
    #resto de 5, seram as notas de 1 
    resto5 = resto10 % 5
   

    print(f"""
        Saque de {saque} reais 
        notas :
        - {notas100} de 100
        - {notas50} de 50
        - {notas10} de 10
        - {notas5} de 5
        - {resto5} de 1""")
else:
    print('VALOR INVÁLIDO')
