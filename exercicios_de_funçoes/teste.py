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

# Criando a lista
lista = [1,2,3,4,5,6,7,8,9]
# Convertendo para Matrix
matrix = criar_matrix(lista)

for i in range(10):
    lista_embaralhada = embaralhar(lista)
    matrix = criar_matrix(lista_embaralhada)
    print(matrix)