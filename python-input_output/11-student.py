#!/usr/bin/python3
"""a class Student that defines a student by:"""


class Student:
    """The class Student which includes a first name, last name and age"""
    def __init__(self, first_name, last_name, age):
        """the first funtion that it will run when creating a class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance"""
        if isinstance(attrs, list):
            for y in attrs:
                for x in self.__dict__:
                    if y == x:
                        return vars(self)[y]
        else:
            return self.__dict__
    def reload_from_json(self, json):
        for x in self.__dict__:
            for y in json.__dict__:
                if x == y:
                    self.__dict__[x] = json.__dict__[y]
        return self.__dict__