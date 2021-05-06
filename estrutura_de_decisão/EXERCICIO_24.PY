#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

#    par ou ímpar;
#    positivo ou negativo;
#    inteiro ou decimal. 

def par_ou_impar (x,y):
    a = x % 2
    b = y % 2

    if a == 0 and b == 0:
        print()
        print(f'{x} é par, {y} é par')
    elif a != 0 and b == 0:
        print()
        print(f'{x} é impar, {y} é par')
    elif a == 0 and b != 0:
        print()
        print(f'{x} é par , {y} é impar')
    elif a != 0 and b != 0:
        print()
        print(f'{x} é impar, {y} é impar')

def negativo_ou_positivo (x,y):
    if x <0 and y <0:
        print()
        print(f'{x} e {y} são negativos')
    elif x > 0 and y > 0:
        print()
        print(f'{x} e {y} são positivos')
    elif x > 0 and y < 0:
        print()
        print(f'{x} é positivo e {y} é negativo')
    elif x < 0 and y > 0:
        print()
        print(f'{x} é negativo e {y} é positivo')
def inteiro_ou_decimal (x,y):
    if x == round(x) and y != round(y):
        print()
        print(f"""
        {x} : valor inteiro  
        {y} : valor decimal """)
    
    elif x != round(x) and y == round(y):
        print()
        print(f"""
        {x} : valor decimal  
        {y} : valor inteiro """)

    elif x == round(x) and y == round(y):
        print()    
        print(f"""
        {x} : valor inteiro  
        {y} : valor inteiro """)
     
    elif x != round(x) and y != round(y):
        print()   
        print(f"""
        {x} : valor decimal   
        {y} : valor decimal  """)

def menu (choice):
    print("""
    QUAL OPERAÇÃO DESAJ-SE FAZER :
    (1) par ou ímpar 
    (2) positivo ou negativo
    (3) inteiro ou decimal
    (4) Sair do programa 
    """)
    choice = eval(input('Digite 1,2 ou 3 para escolher a operação desejada:'))
    while not 1 <= choice <= 4:
        print()
        choice = eval(input('Digite uma opçao entre 1 e 4: '))
    return choice

    # o codigo começa aqui 
valor1 =  float(input('valor 1:'))
valor2 = float(input('valor 2: '))
loop  = 1 
while loop :
    choice =  menu(1)
    if choice == 1:
        a = par_ou_impar(valor1,valor2)
        print(a)
    elif choice == 2:
        a = negativo_ou_positivo(valor1,valor2)
        print(a)
    elif choice == 3:
        a = inteiro_ou_decimal(valor1,valor2)
        print(a)
    elif choice == 4:
        loop = 0
print()
print('Obrigado por usar o programa !')
