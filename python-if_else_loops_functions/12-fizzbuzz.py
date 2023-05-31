#!/usr/bin/python3
def fizzbuzz():
    txt = "{} "
    for num in range(1, 101):
        if num % 3 == 0:
            print(txt.format("Fizz"), end="")
        elif num % 5 == 0:
            print(txt.format("Buzz"), end="")
        elif num % 3 == 0 and num % 5 == 0:
            print(txt.format("FizzBuzz"), end="")
        else:
            print(txt.format(num), end="")
