#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        var = number % -10
        print("{}".format(var), end="")
        return var
    elif number > 0:
        var2 = number % 10
        print("{}".format(var2), end="")
        return var2
    else:
        print("{}".format(number), end="")
        return number
