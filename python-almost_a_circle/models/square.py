#!/usr/bin/python3
"""WWrite the class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return (super().height)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 1:
            raise ValueError("height must be > 0")
        else:
            self.height = value
            self.width = value

    def __str__(self):
        """returns the object Square with all their values"""
        txt = "[Square] ({}) {}/{} - {}"
        rec = txt.format(self.id, self.x, self.y, self.width)
        return rec
