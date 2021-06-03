#Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:

#8  3  4 
#1  5  9
#6  7  2

#Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.

import numpy as np
from random import*


def possibilidades_permutadas(lista):
    multp = 1
    for p in range(1,len(lista) + 1):
        multp = multp * p
    return multp

def embaralhar (lista):
    contador = 0
    verif_num = []
    lista_emabaralhada = []
    while len(lista) > contador:
        cod_num = randint(0,len(lista)-1)
        if cod_num not in verif_num:
            verif_num.append(cod_num)
            contador += 1
            lista_emabaralhada.append(lista[cod_num])
        else:
            continue 
    return lista_emabaralhada  
    

def criar_matrix (lista):
    elementos = np.array(lista)
    matrix = elementos.reshape(3,3)
    return matrix
    

def somar_linhas (lista):
    linha = np.sum(lista, axis=1)
    return linha

def somar_coluna (lista):
    coluna = np.sum(lista, axis=0)
    return coluna

def diagonais(lista):
    diagonal_normal = np.diagonal(lista)
    anti_diagonal = np.fliplr(lista).diagonal()
    return diagonal_normal, anti_diagonal

def somar_diagonais (diagonal, anti_diagonal):
    somar_diagonal = np.sum(diagonal)
    somar_anti = np.sum(anti_diagonal)
    return somar_diagonal, somar_anti


# Criando a lista
lista = [1,2,3,4,5,6,7,8,9]
# Convertendo para Matrix
matrix = criar_matrix(lista)
count = 0
loop = possibilidades_permutadas(lista)

while loop > count:
    
    # soma total das linhas e coluna
    linha = somar_linhas(matrix)
    coluna = somar_coluna(matrix)
    # vetor com os valores da diagonal
    diag, anti_diag = diagonais(matrix)
    #soma das diagonais
    soma_diag, soma_anti = somar_diagonais(diag, anti_diag)
    #comparando linha com coluna
    linha_coluna = np.array_equal(linha,coluna)
    #comparando as duas diagonais
    diag_e_anti = np.array_equal(soma_anti,soma_diag) 
    count += 1

    if linha_coluna == True and diag_e_anti == True:
        if linha[0] == soma_diag:
            print(matrix) 
            print("")
            lista = embaralhar(lista)
            matrix = criar_matrix(lista)
        
    else:
        lista = embaralhar(lista)
        matrix = criar_matrix(lista)
    

# arrumar ainda 