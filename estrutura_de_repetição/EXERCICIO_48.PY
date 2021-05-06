#Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
#Exemplo:
#  12376489
#  => 98467321

lista_inversa = []
num = int(input("Digite o valor: "))

resp = 1
while (resp !=0):
    resp = num // 10
    resto = num % 10
    lista_inversa.append(str(resto))   
    num = resp
lista_inversa = "".join(lista_inversa)
print(int(lista_inversa))