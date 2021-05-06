#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida. 
dia_mes_ano = [int(input('dia: ')),int(input('mês: ')),int(input('ano: '))]

# critérios para um ano ser bissexto

# divisível por 4 
resto4 = dia_mes_ano[2] % 4
# não divisível por 100
resto100 = dia_mes_ano[2] % 100
# não pode ser divisível por 400
resto400 = dia_mes_ano[2] % 400

# verificando o intervalo do mês 
if dia_mes_ano[1] in [1,2,3,4,5,6,7,8,9,10,11,12]:
   
    # meses com daté 31 dias 
    if dia_mes_ano[1] in [1,3,5,7,8,10,12]:
        if dia_mes_ano[0] >= 1 and dia_mes_ano <= 31:
            if dia_mes_ano[2] <= 2020 :
                print(f'Data válida : {dia_mes_ano}')
   
    # meses com até 30 dias 
    elif dia_mes_ano[1] in [4,6,9,11]:
        if dia_mes_ano[0] >= 1 and dia_mes_ano <= 30:
            if dia_mes_ano[2] <= 2020:
                print(f'Data válida : {dia_mes_ano}')
  
   # mês de fevereiro varia com ano bissexto
    elif dia_mes_ano[1] == 2:
        # situação com um possivel ano bissexto 
        if resto4 == 0 and resto100 != 0 or resto400 == 0 :
            #mes com 29 dias em ano bissexto
            if dia_mes_ano[0] >= 1 and dia_mes_ano <= 29:
                if dia_mes_ano[2] <= 2020:
                    print(f'Data válida : {dia_mes_ano}')
        
        # mes com 28 dia fora no ano bissexto 
        elif dia_mes_ano[0] >= 1 and dia_mes_ano <= 28:
            if dia_mes_ano[2] <= 2020:
                print(f'Data válida : {dia_mes_ano}')
else:
    print(f'Data inválida : {dia_mes_ano}')    