#!/usr/bin/python3
"""Adds perimeter and area to rectangle class"""


class Rectangle:
    """it creates a class called Rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """it creates the prototype of the class square"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """function to calculate the area"""
        return self.__height * self.__width

    def perimeter(self):
        """function to calculate the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__height * 2 + self.__width * 2

    def __str__(self):
        """function to return a rectangle made of the # symbol"""
        rec = ""
        if self.__height == 0 or self.__width == 0:
            return rec
        for x in range(self.__height):
            rec = rec + ('#' * self.__width + '\n')
        return rec[:-1]

    def __repr__(self):
        """a funtion that returns a string with what mades the rectangle"""
        rec = "Rectangle({}, {})".format(self.__width, self.__height)
        return rec

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
        del self
