#!/usr/bin/python3
"""Write a function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """a function that creates an object from a file"""
    with open(filename, mode="r") as f:
        o = json.load(f)
        return o
