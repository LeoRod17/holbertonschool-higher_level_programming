#!/usr/bin/python3
import sys
txt = "arguments"
count = len(sys.argv)
if (count < 1):
    print("{} {}.".format(count, txt))
else:
    print("{} {}:".format(count - 1, txt))
    for s in range(1, count):
        print("{}: {}".format(s, sys.argv[s]))
