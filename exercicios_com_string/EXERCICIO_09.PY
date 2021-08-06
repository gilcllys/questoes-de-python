#Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.

#cpf = input("Informe o número de CPF no formato xxx.xxx.xxx-xx: ")
cpf = "158.956.827-31"
modelo_cpf ="123.123.123-12"
# lista[0] = 123 
# lista[1] = . 
# lista[2] = 123 
# lista[3] = . 
# lista[4] = 123 
# lista[5] = -
# lista[6] = 12 

numeros_aceitos = "1234567890"

#validação de tamanho
if len(cpf) == len(modelo_cpf):
    lista = [cpf[0:3],cpf[3],cpf[4:7],cpf[7],cpf[8:11],cpf[11],cpf[12::]]
    #varificando as pontuações
    if lista[1] =="." and lista[3] == "." and lista[5] == "-":
        # verificando os numeros aceitos
        if lista[0] in numeros_aceitos and lista[2] in numeros_aceitos and lista[4] in numeros_aceitos and lista[6] in numeros_aceitos:
            print(f"CPF: {cpf} VALIDADO !")
        
        else:
            print("!Entrada incorreta!")
            print("!Quantidade de dígitos correta!")
            print("!Modelo de cpf no padrão!")  
            print(">Números fora do padrão<")

    
    else:
        print("!Entrada incorreta!")
        print("!Quantidade de dígitos correta!")
        print(">Modelo de cpf fora do padrão<")  

else:
    print("!Entrada incorreta!")
    print(">Quantidade de dígitos incorreta<")


