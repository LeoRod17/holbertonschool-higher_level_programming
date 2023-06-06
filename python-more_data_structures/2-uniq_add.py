#!/usr/bin/python3
def uniq_add(my_list=[]):
    lista = list(set(my_list))
    val1 = 0
    for x in range(len(lista)):
        val1 = val1 + lista[x]
    return val1
