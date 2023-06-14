#!/usr/bin/python3
def matrix_divided(matrix, div):
    mat = matrix.copy
    if not isinstance(div, int) or not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if isinstance(matrix):
        for x in range(len(matrix)):
            for j in range(len(matrix[x])):
                if not isinstance(matrix[j], int) or not isinstance(matrix[j], float):
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                
                