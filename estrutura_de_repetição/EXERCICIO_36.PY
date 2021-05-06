#Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:

#    Montar a tabuada de: 5
#    Começar por: 4
#    Terminar em: 7

# Vou montar a tabuada de 5 começando em 4 e terminando em 7:
#    5 X 4 = 20
#    5 X 5 = 25
#    5 X 6 = 30
#    5 X 7 = 35

tabuada = int(input('Valor da tabuada: '))
valor_inicial = int(input('valor de partidada da tabuada: '))
valor_final = int(input('valor de ecerramento da tabauda: '))

print(f'Montar a tabuada de {tabuada}')
print(f'Começa por: {valor_inicial}')
print(f'Terminar em: {valor_final}')
print()
if valor_final > valor_inicial:
    for i in range(valor_inicial,valor_final+1):
        resultado = tabuada * i 
        print(f"""{tabuada} X {i} = {resultado}""")
else:
    print('!!!!! valores de partida e encerramento estão incorrentos !!!!!')