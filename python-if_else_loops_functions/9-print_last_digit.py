#!/usr/bin/env python3
def print_last_digit(number):
    txt = "{}"
    if number < 0:
        number = number * -1
    num = number % 10
    print(txt.format(num), end="")
    return (num)
