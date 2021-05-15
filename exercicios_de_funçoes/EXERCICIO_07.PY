#Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.


def valorPagamento(valor_atraso, dias_atraso):
    if dias_atraso > 0:
        total_a_pagar = (valor_atraso*1.03) + (valor_atraso*(0.1*dias_atraso))
        pagamento.append(total_a_pagar)
    else:
        total_a_pagar = valor_atraso
        pagamento.append(total_a_pagar)
    print("*"*50)
    print(f"VALOR A PAGAR: R$ {total_a_pagar}")
    print(f"Dias de atraso: {dias_atraso}")
    print("*"*50)
    print("\n")
    
pagamento = []
VALOR = True
while VALOR: 
    valor_atraso = float(input("Digite o valor da prestação: "))
    if valor_atraso == 0:
        VALOR = False
        total_prestacoes = sum(pagamento)
        quantidade_prestacoes = len(pagamento)
        print(f"""
********************************************************************
        TOTAL DE PRESTAÇÕES: {total_prestacoes}
        QUANTIDADE DE PRESTAÇÕES: {quantidade_prestacoes}
*********************************************************************""")
    else:
        dias_atraso = int(input("Digite os dias que a prestação esta atrasada: "))
        valorPagamento(valor_atraso,dias_atraso)


