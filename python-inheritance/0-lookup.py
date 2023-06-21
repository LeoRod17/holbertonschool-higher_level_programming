#!/usr/bin/python3
"""a function that returns the list of available attributes
 and methods of an object"""


def lookup(obj):
    """I use the dir function to get all about the given object"""
    return dir(obj)
