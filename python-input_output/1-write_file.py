#!/usr/bin/python3
"""Write a function that writes a string to a text file (UTF8) and
returns the number of characters written:"""


def write_file(filename="", text=""):
    """a function that write a text in a file and returns the times it wrote"""
    count = 0
    with open(filename, mode="w+") as f:
        w = f.write(text)
        t = f.read()
        for x in text:
            count = count + 1
        return count
