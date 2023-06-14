#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'
A function that prints a square with the character #.
"""


def print_square(size):
    """python3 -c 'print(__import__("my_module").my_function.__doc__)
    a function that prints a square while checking it`s
    value and type
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        for y in range(size):
            print("#", end="")
        print()
