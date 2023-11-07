#!/usr/bin/python3

"""let's get this sh*t Done"""


def append_write(filename="", text=""):
    """append a file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.append(text)
