#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    size = len(my_list)
    if (idx < size and idx >= 0):
        my_list[idx] = element
    return my_list
