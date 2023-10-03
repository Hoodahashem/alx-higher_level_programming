#!/usr/bin/python3
def uppercase(str):
    newline = '\n'

    for char in str:
        var = ord(char)
        if var in range(97, 123):
            char = chr(var - 32)
        else:
            char = char
        print("{}".format(char), end="")
    print("{}".format(newline), end="")
