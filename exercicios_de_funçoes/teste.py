import numpy as np
from random import*

def embaralhar (lista):
    lista_embaralhada = np.random.permutation(lista)
    return lista_embaralhada
    
# modelar a lista no formato de uma matrix 3x3 
def criar_matrix (lista):
    elementos = np.array(lista)
    matrix = elementos.reshape(3,3)
    return matrix

def repetidas (lista,nova_lista):
    for comp in nova_lista:
        comparando = np.equal(lista,nova_lista)
        if comparando == True:
            valor = True
            return valor
            break
        else:
            continue
    


# Criando a lista
lista = [1,2,3,4,5,6,7,8,9]
# Convertendo para Matrix
matrix = criar_matrix(lista)
nova_lista = [