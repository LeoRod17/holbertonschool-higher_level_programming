#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'
Write a function that prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """python3 -c 'print(__import__("my_module").my_function.__doc__)
    a function that prints the full name of a person by
    their first and last name it has to be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    txt = "My name is {} {}"
    print(txt.format(first_name, last_name))
