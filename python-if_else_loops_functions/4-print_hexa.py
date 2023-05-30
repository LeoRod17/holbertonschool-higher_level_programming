#!/usr/bin/python3
txt = "{} = {} \n"
for number in range(0, 99):
    print(txt.format(number, hex(number)), end=" ")
