#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    index = len(sys.argv)
    if index == 1:
        print("{:d} arguments.".format(index - 1))
    elif index == 2:
        print("{:d} argument:".format(index - 1))
    else:
        print("{:d} arguments:".format(index - 1))
    for i in range(1, index):
        print("{:d}: {:s}".format(i, sys.argv[i]))
