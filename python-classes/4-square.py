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

    def __init__(self, size=0):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)
        this is a constructor it is for recieving the values and
        creating the class
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    """python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
    I added some exceptions to the value of size
    First: the value because a square can not be with minus size
    Second: the size needs to be an int to do the calculations
    """
    def area(self):
        return self.__size * self.__size
