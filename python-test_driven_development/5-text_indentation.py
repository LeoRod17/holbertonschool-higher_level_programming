#!/usr/bin/python3
""" a function that prints a text with new lines after this
characters: (.), (?) and (:)
"""


def text_indentation(text):
    """the text will separate and print each time a special
    symbol appears
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    txt = ""
    token = 0
    for x in range(len(text)):
        txt = txt + text[x]
        if text[x] == "." or text[x] == "?" or text[x] == ":" and token == 0:
            while text[x + 1] == " ":
                x = x + 1
            print("{}".format(txt))
            print()
            txt = ""
    print("{}".format(txt))
