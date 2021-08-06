#Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

#Data de Nascimento: 29/10/1973
#Você nasceu em  29 de Outubro de 1973.

dia = int(input("dia:"))
mes = int(input("mes:"))
ano = int(input("ano:"))

meses = ["Janeiro", "Fevereiro", "Março", "Abril","Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
codigo_mes = meses[mes-1]

if mes < 10 and dia <10:
    print(f"Data de Nascimento: 0{dia}/0{mes}/{ano}")
    print(f"Você nasceu em 0{dia} de {codigo_mes} de {ano}")
elif mes<10:
    print(f"Data de Nascimento: {dia}/0{mes}/{ano}")
    print(f"Você nasceu em {dia} de {codigo_mes} de {ano}")
elif dia <10:
    print(f"Data de Nascimento: 0{dia}/{mes}/{ano}")
    print(f"Você nasceu em 0{dia} de {codigo_mes} de {ano}")
else:
    print(f"Data de Nascimento: {dia}/{mes}/{ano}")
    print(f"Você nasceu em {dia} de {codigo_mes} de {ano}")
