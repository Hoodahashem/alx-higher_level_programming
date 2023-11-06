#!/usr/bin/python3

"""let's wrap this up quickly"""


def inherits_from(obj, a_class):
    """docstring for inherits_from"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
