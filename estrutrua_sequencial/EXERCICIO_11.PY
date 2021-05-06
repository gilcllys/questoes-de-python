#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

#- o produto do dobro do primeiro com metade do segundo .
#- a soma do triplo do primeiro com o terceiro.
#- o terceiro elevado ao cubo.
int1 = int(input("inteiro 1: "))
int2 = int(input('inteiro 2: '))
real = float(input('real : '))
#- o produto do dobro do primeiro com metade do segundo .
c1 = (int1*2)*(int2/2)
#- a soma do triplo do primeiro com o terceiro.
c2  = (int1*3) + real
#- o terceiro elevado ao cubo.
c3 = real ** 3
print('-'*100)
print('o produto do dobro do primeiro com metade do segundo')
print(c1)
print('-'*100)
print('a soma do triplo do primeiro com o terceiro.')
print(c2)
print('-'*100)
print('o terceiro elevado ao cubo.')
print(c3)
print('-'*100)
