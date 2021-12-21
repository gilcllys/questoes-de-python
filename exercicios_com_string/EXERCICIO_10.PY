#Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.

um_a_nove = ["zero","um","dois","três","quatro","cinco","seis","sete","oito","nove"]
multp_de_10 = ["Dez","Vinte","Trinta","Quarenta","Ciquenta","Sessenta","Setenta","Oitenta","Noventa"]
onze_a_dezenove = ["Onze","Doze","Treze","Quatorze","Quinze","Dezeseis","Dezessete","Dezoito","Dezenove"]
while True:
    user = int(input("Digite um número de 0 a 99 para ver a forma extensa dele: "))

    mult_10 = user % 10
    conversao = user // 10

    if 0 <= user <= 9:
        print(um_a_nove[user])
    elif 11 <= user <= 19:
        print(onze_a_dezenove[ user - 11])
    elif mult_10 == 0:
        print(multp_de_10[conversao-1])
    elif user > 20:
        print(f'{multp_de_10[conversao-1]} e {um_a_nove[mult_10]}')