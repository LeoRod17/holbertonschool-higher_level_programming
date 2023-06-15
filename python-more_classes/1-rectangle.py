#!/usr/bin/python3
"""Creating atributes for  rectangle class"""


class Rectangle:
    """it creates a class called Rectangle"""
    def __init__(self, width=0, height=0):
        """it creates the prototype of the class square"""
        self.__width = width
        self.__height = height
    
    def width(self):
        """getter of width"""
        return self.__width
    def width(self, value):
        """setter of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
    def height(self):
        """getter of height"""
        return self.__height
    def height(self, value):
        """setter of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__width = value
