#!/usr/bin/python3
"""Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:"""


def append_write(filename="", text=""):
    """a function that write a text in a file and returns the times it wrote"""
    count = 0
    with open(filename, mode="a+") as f:
        w = f.write(text)
        t = f.read()
        for x in text:
            count = count + 1
        return count
