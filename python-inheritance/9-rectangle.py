#!/usr/bin/python3
"""Creating a Child of base geometry class called Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """the class who will inherit from basegeometry"""
    def __init__(self, width, height):
        """the first function the class will use"""
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)

    def area(self):
        """a function that gives the area"""
        return self.__width * self.__height

    def __str__(self):
        """a function to print the rectangle with its values"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
