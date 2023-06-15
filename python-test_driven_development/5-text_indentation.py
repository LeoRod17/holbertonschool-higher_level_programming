#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    txt = ""
    for x in text:
        txt = txt + x
        if x == "." or x == "?" or x == ":":
            print("{}".format(txt))
            print()
            txt = ""
    print("{}".format(txt))
