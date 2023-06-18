#!/usr/bin/python3
def matrix_divided(matrix, div):
    mat = [0] * len(matrix)
    if  type(div) is  int or type(div) is float:
        if div == 0 :
            raise ZeroDivisionError("division by zero")
        for x in range(len(matrix)):
                mat[x] = list(map(lambda y: y / div, matrix[x]))
    else:
        raise TypeError("div must be a number")
    return mat 
                