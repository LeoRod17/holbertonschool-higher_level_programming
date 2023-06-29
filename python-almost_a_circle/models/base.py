#!/usr/bin/python3
"""Write the first class Base:"""
import json
import os


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

    @staticmethod
    def from_json_string(json_string):
        lista = []
        if json_string is None:
            return lista
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Square":
            form = cls(5)
        else:
            form = cls(5, 7)
        form.update(**dictionary)
        return form

    @classmethod
    def load_from_file(cls):
        """Classs method that returns a list of instances:"""
        filename = str(cls.__name__) + ".json"
        lista = []
        if os.path.exists(filename):
            with open(filename, mode="r") as f:
                lista = cls.from_json_string(f.read())
                r = []
                for x in lista:
                    r.append(cls.create(**x))
                return r
        else:
            return []
