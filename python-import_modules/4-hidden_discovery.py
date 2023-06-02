#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    text = dir(hidden_4)
    size = len(text)
    for x in range(0, size):
        if text[x].startswith('__'):
            text
        else:
            print("{}".format(text[x]))
