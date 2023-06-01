#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    txt = "arguments"
    txt2 = "argument"
    count = len(sys.argv)
    if (count == 1):
        print("{} {}.".format(count - 1, txt))
    elif count == 2:
        print("{} {}:".format(count - 1, txt2))
        print("{}: {}".format(count - 1, sys.argv[1]))
    else:
        print("{} {}:".format(count - 1, txt))
        for s in range(1, count):
            print("{}: {}".format(s, sys.argv[s]))
