#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'
this is proyect is to learn how to make chekers and tests to try
"""


def add_integer(a, b=98):
    """python3 -c 'print(__import__("my_module").my_function.__doc__)
    a function that adds two ints and sends a error mesage if not an
    int or float converts floats into ints
    """

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return (a + b)
