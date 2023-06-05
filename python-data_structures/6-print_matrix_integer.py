#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    txt ="{:d}"
    for x in range (len(matrix)):
        for j in range (len(matrix[x])):
            print(txt.format(matrix[x][j]), end="")
        print()