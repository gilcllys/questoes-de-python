#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. 
while True:
    sexo = input('digite F ou f (Feminino) / M ou m (Masculino) :')
    sexo = sexo.upper()
    if sexo == "F" :
        print('sexo FEMININO')
    elif sexo == "M":
        print('sexo MASCULINO')
    else:
        print('SEXO INVÁLIDO')
            