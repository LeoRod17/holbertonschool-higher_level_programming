#!/usr/bin/python3
"""a function that writes an Object to a text file, using
a JSON representation:"""
import json


def save_to_json_file(my_obj, filename):
    """writes a file for a given object an remakes the file if it not exists"""
    with open(filename, mode="w+") as f:
        json.dump(my_obj, f)
