#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for a in range(0, x):
        try:   
            print("{:d}".format(my_list[a]), end="")
        except IndexError:
                return a
    print()
    return x 
