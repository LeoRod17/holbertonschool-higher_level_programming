#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if my_list:
        txt = "{:d}"
        size = len(my_list)
        my_list.reverse
        for x in range(0, size):
            print(txt.format((my_list[x])))
