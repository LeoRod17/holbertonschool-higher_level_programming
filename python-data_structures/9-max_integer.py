#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        val1 = 0
        size = len(my_list)
        my_list.sort()
        for x in range(0, size):
            if x == size - 1:
                val1 = my_list[x]
        return ("{:d}".format(val1))
    else:
        return None
