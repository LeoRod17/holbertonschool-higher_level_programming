#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    c = a_dictionary.copy()
    for x in c:
        c[x] = a_dictionary.get(x) * 2
    return c
