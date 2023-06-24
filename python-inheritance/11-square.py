#!/usr/bin/python3
"""Creating a Child of Rectangle class that is a
child of base_geometry called Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """the class square with width and height are the same
    in one value called size"""
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size
        Rectangle.integer_validator(self, "size", size)

    def __str__(self):
        """a function to print the Square with its values"""
        return "[Square] {}/{}".format(self.__size, self.__size)
