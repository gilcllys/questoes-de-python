#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano =  int(input('Digite o ano para verificar se é bissexto ou não: '))

# critérios para um ano ser bissexto

# divisível por 4 
resto4 = ano % 4
# não divisível por 100
resto100 = ano % 100
# não pode ser divisível por 400
resto400 = ano % 400

if resto4 == 0 and resto100 != 0 or resto400 == 0 :
    print (f' O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto') 

