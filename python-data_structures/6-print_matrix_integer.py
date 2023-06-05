#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    txt = "{:d} "
    for x in range(len(matrix)):
        for j in range(len(matrix[x])):
            if x != len(matrix) and j != len(matrix[x]) - 1:
                print(txt.format(matrix[x][j]), end="")
            else:
                print("{:d}".format(matrix[x][j]), end="")
        print()
