#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    txt = "arguments"
    count = len(sys.argv)
    if (count == 1):
        print("{} {}.".format(count - 1, txt))
    else:
        print("{} {}:".format(count - 1, txt))
        for s in range(1, count):
            print("{}: {}".format(s, sys.argv[s]))
