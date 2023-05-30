#!/usr/bin/python3
txt1 = "{}{}, "
txt2 = "{}{}\n"
for number in range(0, 10):
    for num in range(number + 1, 10):
        if number == 8 and num == 9:
            print(txt2.format(number, num), end="")
        else:
            print(txt1.format(number, num), end="")
