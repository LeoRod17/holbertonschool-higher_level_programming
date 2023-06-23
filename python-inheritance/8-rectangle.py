#!/usr/bin/python3
"""Creating a Child of base geometry class called Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """the class who will inherit from basegeometry"""
    def __init__(self, width, height):
        BaseGeometry.integer_validator("width", width)
        self.__width = width

        BaseGeometry.integer_validator("height", height)
        self.__height = height
        