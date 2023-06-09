#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    r = [0] * list_length
    try:
        for x in range(list_length):
            try:
                r[x] = my_list_1[x] / my_list_2[x]
            except ValueError:
                print("wrong type")
            except TypeError:
                print("wrong type")
            except IndexError:
                print("out of range")
            except ZeroDivisionError:
                print("division by 0")
    finally:
        return r
