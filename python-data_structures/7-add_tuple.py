#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lista = [0, 0]
    size1 = len(tuple_a)
    size2 = len(tuple_b)
    for x in range(size1):
        if x > 1:
            break
        lista[x] += tuple_a[x]
    for s in range(size2):
        if s > 1:
            break
        lista[s] += tuple_b[s]
    return (lista[0], lista[1])
