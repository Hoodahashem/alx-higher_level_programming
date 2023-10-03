#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lol = number % -10
    if lol == 0:
        print(f"Last digit of {number} is {lol} and is 0")
    else:
        print(f"Last digit of {number} is {lol} and is less than 6 and not 0")
elif number == 0:
    print(f"Last digit of {number} is {number} and is 0")
else:
    lol2 = number % 10
    if lol2 < 6:
        print(f"Last digit of {number} is {lol2} and is less than 6 and not 0")
    if lol2 > 5:
        print(f"Last digit of {number} is {lol2} and is greater than 5")
    if lol2 == 0:
        print(f"Last digit of {number} is {lol2} and is 0")
