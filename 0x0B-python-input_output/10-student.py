#!/usr/bin/python3
"""let's get this sh*t Done"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

def to_json(self, attrs=None):
    """Convert a Python object to a JSON string"""
    if attrs is None:
        return self.__dict__
    else:
        my_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                my_dict[attr] = getattr(self, attr)
        return my_dict
