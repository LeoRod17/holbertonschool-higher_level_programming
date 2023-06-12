#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'
this is a task for holberton school were i have to creat a class
with a private attribute called size
"""


class Square():
    """(python3 -c 'print(__import__("my_module").MyClass.__doc__)')
    This is an class of a square with just one attribute called size
    size: it is an attribute to know the size of the square
    """
    def __init__(self, size):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)
        this is a constructor it is for recieving the values and
        creating the class
        """
        self.__size = size
    """python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
        I do not know why you want me to separate this documentation
        in an outside and inside a function but here you have it
    """
