#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    size = len(my_list)
    lista = [0] * size
    for x in range(0, size):
        if my_list[x] % 2 == 0:
            lista[x] = True
        else:
            lista[x] = False
    return (lista)
