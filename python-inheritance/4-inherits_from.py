#!/usr/bin/python3
""" a function that returns True if the object is an instance of a class
that inherited (directly or indirectly) from the specified class ; otherwise False."""


def inherits_from(obj, a_class):
    """the function return checks if the object is a subclass
    and if is the type is different of a_class"""
    if issubclass(type(obj),  a_class) and type(obj) != a_class:
        return True
    else:
        return False
