#!/usr/bin/python3
def uppercase(str):
    newline = '\n'
    def uppercaselol(chrs):
        var = ord(chrs)
        if var in range(65, 91):
            return chrs
        else:
            return chr(var + 31)
    for lol in str:
        print("".format(uppercaselol(lol)), end="")
    print("{}".format(newline), end="")
