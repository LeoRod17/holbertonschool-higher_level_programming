#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matriz = matrix.copy()
    for x in range(len(matrix)):
        matriz[x] = list(map(lambda y: y * y, matrix[x]))
    return matriz
