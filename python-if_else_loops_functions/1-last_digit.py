#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    number = number * -1
    num = number % 10
    number = number * -1
    num = num * -1
else:
    num = number % 10
if num < 6 and num != 0:
    print(f"Last digit of {number} is {num} and is less than 6 and not 0")
if num == 0:
    print(f"Last digit of {number} is {num} and is 0")
if num > 5:
    print(f"Last digit of {number} is {num} and is greater than 5")
