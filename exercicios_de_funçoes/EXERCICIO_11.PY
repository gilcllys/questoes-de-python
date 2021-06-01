#Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.


def conversor_mes_extenso (data):
    # Todos os meses do ano 
    mes = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    # convertendo a string em uma lista divida no "/"
    data = data.split("/")
    # codigo para achar o mês na lista   
    mes_data = int(data[1]) - 1

    print(f"Data: {data[0]} de {mes[mes_data]} de {data[2]}")


data = input("informe a data que deseja converter, escreva no formato (DD/MM/AAAA): ")

conversor_mes_extenso(data)