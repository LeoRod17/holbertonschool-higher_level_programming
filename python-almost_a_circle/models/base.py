#!/usr/bin/python3
"""Write the first class Base:"""
import json


class Base():
    """The base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        lista = []
        if list_objs is not None:
            for x in list_objs:
                lista.append(x.to_dictionary())
        filename = str(cls.__name__) + ".json"
        with open(filename, mode="w+") as f:
            f.write(cls.to_json_string(lista))
