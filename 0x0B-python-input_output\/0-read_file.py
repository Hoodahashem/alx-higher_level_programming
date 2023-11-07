#!/usr/bin/python3

"""let's get this sh*t Done"""


def read_file(filename=""):
    """Read a file"""
    with open(filename, "r") as f:
        return f.read()
