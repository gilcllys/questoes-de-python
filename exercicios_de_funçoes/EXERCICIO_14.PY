#Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:

#8  3  4 
#1  5  9
#6  7  2

#Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.



# ALGORITMO INCOMPLETO
from typing import Tuple
import numpy as np
from random import*
import itertools

from numpy.core.fromnumeric import diagonal


class Matrix:
    def __init__(self):
        self.lista = [1,2,3,4,5,6,7,8,9]

    def CriarMatrix (self,matrix):
        self.matrix =  matrix
        vetor = np.array(self.matrix)
        nova_matrix = vetor.reshape(3,3)
        return nova_matrix

    
    def Embaralhar (self):
        valores_permutados = itertools.permutations(self.lista)
        lista = list(valores_permutados)
        return lista

    def SomarLinhasHorizontais(self, matrix):
        self.matrix = matrix
        return np.sum(self.matrix,1)
    def SomarLinhasVerticais(self, matrix):
        self.matrix = matrix
        return np.sum(self.matrix,0)
    def SomarDiagonal(self, matrix):
        self.matrix = matrix
        diagonal = np.diagonal(self.matrix)
        return  np.sum(diagonal)
    def SomarAntiDiagonal(self, matrix):
        self.matrix = matrix
        anti_diagonal = np.fliplr(self.matrix).diagonal()
        return np.sum(anti_diagonal)
    def comparar_linha_com_coluna(self,linha,coluna):
        self.linha = linha
        self.coluna = coluna
        return np.array_equal(self.linha,self.coluna)


matrix = Matrix()
permutacoes = matrix.Embaralhar()

for matrizes in permutacoes:
    quadrado_magico = matrix.CriarMatrix(matrizes)
    diag = matrix.SomarDiagonal(quadrado_magico)
    anti_diag = matrix.SomarAntiDiagonal(quadrado_magico)
    
    if diag == anti_diag:
        linha = matrix.SomarLinhasHorizontais(quadrado_magico)
        coluna = matrix.SomarLinhasVerticais(quadrado_magico)
        comparar = matrix.comparar_linha_com_coluna(linha,coluna)
        if comparar == True:
            if diag == linha[0]:
                print("quadrado_magico: ", diag,linha[0])
            else:
                pass
        else:
            pass
    else:
        pass



