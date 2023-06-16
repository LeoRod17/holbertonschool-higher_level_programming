#!/usr/bin/python3
"""A function that prints a text with new lines after this
characters: (.), (?) and (:)
"""


def text_indentation(text):
    """the text will separate and print each time a special
    symbol appears
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    txt = ""
    for x in range(len(text)):
        txt = txt + text[x]
        if text[x] == "." or text[x] == "?" or text[x] == ":":
            print("{}\n".format(txt))
            txt = ""
            
    print("{}".format(txt))
