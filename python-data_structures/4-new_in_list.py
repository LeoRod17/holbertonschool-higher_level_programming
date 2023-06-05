#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copia = my_list.copy()
    size = len(copia)
    if (idx < size and idx >= 0):
        copia[idx] = element
    return my_list
