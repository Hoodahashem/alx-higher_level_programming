#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        var = number % -10
        print("{}".format(number), end="")
        return number
    elif number > 0:
        var = number % 10
        print("{}".format(number), end="")
        return number
    else:
        print("{}".format(number), end="")
        return number
