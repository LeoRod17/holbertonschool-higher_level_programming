#!/usr/bin/python3
def uppercase(str):
    txt = "{}"
    for x in str:
        x = ord(x)
        if x > 96 and x <= 123:
            x = x - 32
        print(txt.format(chr(x)), end="")
    print()
