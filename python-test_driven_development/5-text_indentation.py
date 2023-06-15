#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    txt = ""
    for x in range (len(text)):
        txt = txt + text[x]
        if text[x] == "." or text[x] == "?" or text[x] == ":":
            while text[x + 1] == " ":
                x = x + 1
            print("{}".format(txt))
            print()
            txt = ""
            
    print("{}".format(txt))
