#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16
numero = int(input('Valor de para fatorar :'))
resultado = 1
loop = True
while loop :
    if 0 < numero <= 16:
        for valor in range(1,numero+1):
            resultado *= valor
        print(f"""
        Fatorial ({numero}) = {resultado}""")
        
    elif numero == 0:
        print(f"""
        Fatorial ({numero}) = 1""")
    else:
        print('Valor incorreto')