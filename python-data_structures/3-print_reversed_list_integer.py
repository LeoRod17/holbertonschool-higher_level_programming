#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if my_list:
        txt = "{:d}"
        my_list.reverse()
        for x in range(0, len(my_list)):
            print(txt.format(my_list[x]))
