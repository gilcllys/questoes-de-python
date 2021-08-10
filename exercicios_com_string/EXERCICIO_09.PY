#Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.

cpf = input("Informe o número de CPF no formato xxx.xxx.xxx-xx: ")
#cpf = "158.956.827-31"

modelo_cpf ="123.123.123-12"

#todos os numeros aceitos no cpf
numeros_aceitos = "1234567890"

#função validadora 
def validador(fatia_cpf):
    for numeros in fatia_cpf:
        if numeros in numeros_aceitos:
            return True
        else:
            return False
            break
#status do validador
validacao = False        

#validação de tamanho
if len(cpf) == len(modelo_cpf):
    
    #fatias do cpf
    lista = [cpf[0:3],cpf[3],cpf[4:7],cpf[7],cpf[8:11],cpf[11],cpf[12:]]
    # lista[0] = 123 
    # lista[1] = . 
    # lista[2] = 123 
    # lista[3] = . 
    # lista[4] = 123 
    # lista[5] = -
    # lista[6] = 12 
    
    #varificando as pontuações
    if lista[1] == "." and lista[3] == "." and lista[5] == "-":
        # verificando os numeros aceitos
        for fatia in range(0,6,2):
            validacao = validador(lista[fatia])
            if validacao == True:
                validacao = True
                continue
            else:
                validacao = False
                break
        if validacao == True:
            print(f"CPF: {cpf} - VALIDADO !")
        
        else:
            print(f"CPF: {cpf} - INVALIDADO !")
            print("!Entrada incorreta!")
            print("!Quantidade de dígitos correta!")
            print("!Modelo de cpf no padrão!")  
            print(">Números fora do padrão<")

    
    else:
        print(f"CPF: {cpf} - INVALIDADO !")
        print("!Entrada incorreta!")
        print("!Quantidade de dígitos correta!")
        print(">Modelo de cpf fora do padrão<")  

else:
    print(f"CPF: {cpf} - INVALIDADO !")
    print("!Entrada incorreta!")
    print(">Quantidade de dígitos incorreta<")

