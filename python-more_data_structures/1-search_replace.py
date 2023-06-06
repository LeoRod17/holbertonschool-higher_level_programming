#!/usr/bin/python3
def search_replace(my_list, search, replace):
        lista = [0] * len(my_list)
        for x in range(len(my_list)):
            if my_list[x] == search:
                lista[x] = replace
            else:
                lista[x] = my_list[x]
        return lista
