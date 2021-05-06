#Um posto está vendendo combustíveis com a seguinte tabela de descontos:

#    Álcool:
#    até 20 litros, desconto de 3% por litro
#    acima de 20 litros, desconto de 5% por litro

#    Gasolina:
#    até 20 litros, desconto de 4% por litro
#    acima de 20 litros, desconto de 6% por litro
 
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90. 

def menu (choice):
    menu = eval(input("""
    Escolha entre álcool em gasolina:
    (1) gasolina 
    (2) álcool
    (3) Sair do programa  
    
    Digite 1 ou 2 para escolher :"""))

    while not  3 >= menu >= 1:
        print()
        menu = eval(input('Digite 1,2 ou 3 :'))
        
    else:
        return menu
# função para calculo da quantidade de álcool 
def alcool (litros):
        if litros > 0 and litros <= 20:
            preco = (litros*1.90)*0.97
            return preco
        elif litros > 20 and litros > 0 :
            preco = preco = (litros*1.90)*0.95
            return preco
        elif litros < 0:
            print('VALOR INVÁLIDO')
# função para calculo da quantidade de gasolina
def gasolina (litros):
        if litros > 0 and litros <= 20:
            preco = (litros*1.90)*0.96
            return preco
        elif litros > 20 and litros > 0:
            preco = preco = (litros*1.90)*0.94
            return preco
        elif litros < 0:
            print('VALOR INVÁLIDO')

# início do pragrama 
loop =True
print()
while loop:
    choice =  menu(1)
    if choice == 1 :
        print()
        volume = float(input(" Valor do volume (litros) do combustível que deseja comprar : "))
        preco = gasolina(volume)
        print()
        print(50*'*')
        print('Comprovante do resultado da compra de GASOLINA')
        print(f"""
        Volume: {volume} litros
        preço = R$ {round(preco,2)}""")
        print(50*'*')
    elif choice == 2:
        print()
        volume = float(input(" Valor do volume (litros) do combustível que deseja comprar : "))
        preco = alcool(volume)
        print()
        print(50*'*')
        print('Comprovante do resultado ÁLCOOL')
        print(f"""
        Volume: {volume} litros
        preço = R$ {round(preco,2)}""")
        print(50*'*')
    elif choice == 3:
        loop = False
print()
print('obrigado por usar o programa ')