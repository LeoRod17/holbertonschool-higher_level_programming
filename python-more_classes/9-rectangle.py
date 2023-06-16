#!/usr/bin/python3
"""Adds calculate the bigger rectangle"""


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
        lista = [0] * self.__width
        if self.__height == 0 or self.__width == 0:
            return rec
        for x in range(self.__height):
            rec = rec + (str(self.print_symbol) * self.__width + '\n')
        return rec[:-1]

    def __repr__(self):
        """a function that returns a string with what mades the rectangle"""
        rec = "Rectangle({}, {})".format(self.__width, self.__height)
        return rec

    def __del__(self):
        """a function that prints a a goodbye before deleting the rectangle
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
        del self

    def bigger_or_equal(rect_1, rect_2):
        """a funtion that compare two rectangle for their area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        a1 = Rectangle.area(rect_1)
        a2 = Rectangle.area(rect_2)
        if a1 > a2:
            return rect_1
        if a2 > a1:
            return rect_2
        if a1 == a2:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """a function that creates a square in the rectangle class"""
        return cls(size, size)
