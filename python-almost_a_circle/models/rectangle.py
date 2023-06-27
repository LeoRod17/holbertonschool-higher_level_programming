#!/usr/bin/python3
"""WWrite the class Rectangle that inherits from Base:"""
from models.base import Base


class Rectangle(Base):
    """The class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 1:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 1:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """a function that returns the area of rectangle"""
        return (self.width * self.height)

    def display(self):
        """creating the square out of #"""
        rec = ""
        rec = rec + ('\n' * self.y)
        if self.height == 0 or self.width == 0:
            return rec
        for x in range(self.__height):
            rec = rec + (" " * self.x)
            rec = rec + ('#' * self.__width + '\n')
        print(rec[:-1])

    def __str__(self):
        txt = "[Rectangle] ({}) {}/{} - {}/{}"
        rec = txt.format(self.id, self.x, self.y, self.width, self.height)
        return rec

    def update(self, *args, **kwargs):
        """a function that updates the rectangle"""
        if args:
            for x in range(0, args):
                if x == 0:
                    self.id = args[0]
                if x == 1:
                    self.width = args[1]
                if x == 2:
                    self.height = args[2]
                if x == 3:
                    self.x = args[3]
                if x == 4:
                    self.y = args[4]
        else:
            for x, y in kwargs.items():
                if x == "id":
                    self.id = y
                if x == "width":
                    self.width = y
                if x == "height":
                    self.height = y
                if x == "x":
                    self.x = y
                if x == "y":
                    self.y = y

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle:"""
        dic = {'x': self.x, 'y': self.y, 'id': self.id,
               'height': self.height, 'width': self.width}
        return dic
