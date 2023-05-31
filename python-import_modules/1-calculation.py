#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as cal
    txt1 = "{} + {} = {}"
    txt2 = "{} - {} = {}"
    txt3 = "{} / {} = {}"
    txt4 = "{} * {} = {}"
    a = 10
    b = 5
    print(txt1.format(a, b, cal.add (a, b)))
    print(txt2.format(a, b, cal.sub(a, b)))
    print(txt4.format(a, b, cal.mul(a, b)))
    print(txt3.format(a, b, cal.div(a, b)))
    