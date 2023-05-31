#!/usr/bin/python3
if __name__ == "__main__":
    txt ="{} + {} = {}"
    from add_0 import add
    a = 1
    b = 2
    print(txt.format(a, b, add(a, b)))
