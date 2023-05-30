#!/usr/bin/python3
number = 0
txt = "{}"
for number in range(97, 123):
    if number != 101 and number != 113:
        print(txt.format(chr(number)), end="")
