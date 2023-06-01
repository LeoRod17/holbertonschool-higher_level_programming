#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    num = 0
    size = len(sys.argv)
    if size > 1:
        for s in range(1, size):
            num = int(sys.argv[s])
            sum = sum + num
        print("{}".format(sum))
    else:
        print("{}".format(0))
