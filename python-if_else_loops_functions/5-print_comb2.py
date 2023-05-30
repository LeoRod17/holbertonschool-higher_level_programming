#!/usr/bin/python3
txt1 = "{}, "
txt2 = "{}\n"
for number in range(0, 100):
    if number <= 98:
        print(txt1.format(str(number).zfill(2)), end="")
    else:
        print(txt2.format(number), end="")
