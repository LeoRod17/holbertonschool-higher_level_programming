#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    size = len(my_list)
    if (idx < size and idx > 0):
        for x in range(0, size):
            if x == idx:
                del my_list[x]
    return my_list
