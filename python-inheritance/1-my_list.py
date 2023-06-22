#!/usr/bin/python3


class MyList(list):
    """ a function that inherits from list"""

    def print_sorted(self):
        print(sorted(self))
