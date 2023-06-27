#!/usr/bin/python3
"""WWrite the class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.update(width=value, height=value)

    def __str__(self):
        """returns the object Square with all their values"""
        txt = "[Square] ({}) {}/{} - {}"
        rec = txt.format(self.id, self.x, self.y, self.width)
        return rec

    def update(self, *args, **kwargs):
        """a function that updates the Square"""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
                self.height = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for x, y in kwargs.items():
                if x == "id":
                    self.id = y
                if x == "size":
                    self.height = y
                    self.width = y
                if x == "x":
                    self.x = y
                if x == "y":
                    self.y = y
