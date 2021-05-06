#Faça um Programa que leia três números e mostre-os em ordem decrescente.
import random
primeiro = round(random.uniform(0,15),2)
segundo  = round(random.uniform(0,15),2)
terceiro = round(random.uniform(0,15),2)
lista =  [primeiro,segundo,terceiro]
print(f'valores antes da ordem {lista}')

# situações onde o maior valor pode se encontrar dentro da variável lista 

#se o maior numéro estiver na posição [0] da variável lista 
if max(lista) == lista [0]:
    # nesse caso vamos orginar para os valores [lista[0],lista[1],lista[2]]
    if lista[1] > lista[2]:
        print(f'os valores em ordem decrescente são {lista}')
    # nesse caso vamos organizar para os valores [lista[0],lista[2],lista[1]]
    elif lista[2] > lista[1]:
        caixa = lista[1]
        lista[1] = lista[2]
        lista[2] = caixa
        print(f'os valores em ordem decrescente são {lista}')        
#se o maior numéro estiver na posição [1] da variável lista 
elif max(lista) == lista [1]:
    #nesse caso vamos organizar para os valores [lista[1],lista[0],lista[2]]
    if lista[0] > lista[2]:
        caixa = lista[0]
        lista[0] = lista [1]
        lista[1] = caixa
        print(f'os valores em ordem decrescente são {lista}')
    #nesse caso vamos organizar para os valores [lista[1],lista[2],lista[0]]
    elif lista[2] > lista[0]:
        caixa = lista [0]
        lista[0] = lista[1]
        lista[2] = caixa
        print(f'os valores em ordem decrescente são {lista}')
#se o maior numéro estiver na posição [2] da variável lista 
elif max(lista) == lista [2]:
    #nesse caso vamos organizar para os valores [lista[2],lista[0],lista[1]]
    if lista[0] > lista [1]:
        caixa = lista[0]
        caixa2 = lista[1]
        lista[0] = lista[2]
        lista[1] = caixa
        lista[2] = caixa2
        print(f'os valores em ordem decrescente são {lista}')
    #nesse caso vamos organizar para os valores [lista[2],lista[1],lista[0]]
    elif lista[1] > lista[0]:
        caixa = lista[0]
        lista [0] = lista[2]
        lista[2] = caixa
        print(f'os valores em ordem decrescente são {lista}')
    
