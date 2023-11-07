#!/usr/bin/python3

"""let's get this sh*t Done"""


def write_file(filename="", text=""):
    """Write a file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
