#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return (1)
    if b < 0:
        a = 1/a
        b = -b
    s = a
    for x in range(1, b):
        if (a > 0):
            a = a * s
        else:
            a = - a
            a = a * s
            a = - a
    return (a)
