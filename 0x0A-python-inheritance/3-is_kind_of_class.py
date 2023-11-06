#!/usr/bin/python3

"""let's create a new function!"""


def is_kind_of_class(obj, a_class):
    """docstring for is_kind_of_class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
