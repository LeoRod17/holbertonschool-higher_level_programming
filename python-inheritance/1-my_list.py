#!/usr/bin/python3
"""Write a class MyList that inherits from list"""


class MyList(list):
    """ a class that inherits from list"""
    def print_sorted(self):
        """A function that prints the sorted list withouth modifing it"""
        print(sorted(self))
