#!/usr/bin/python3
"""a function that reads a text file (UTF8) and prints it to stdout:"""


def read_file(filename=""):
    """a function that reads a text file and prints it"""
    with open(filename) as f:
        r = f.read()
        print(r)
    f.closed
