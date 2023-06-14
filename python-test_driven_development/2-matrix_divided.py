#!/usr/bin/python3
def matrix_divided(matrix, div):
    mat = [0] * len(matrix)
    if  type(div) is not int or type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0 :
        raise ZeroDivisionError("division by zero")
    for x in range(len(matrix)):
        for j in range(len(matrix[x])):
           if type(matrix[j]) is not int or type(matrix[j]) is not float :
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        mat[x,j] = matrix[x,j] / div
    return mat
                
                