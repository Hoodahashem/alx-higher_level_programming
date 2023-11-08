#!/usr/bin/python3
"""let's get this sh*t Done"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Converts attributes to json representation"""
        if attrs is None:
            return self.__dict__
        else:
            dict = {}
            for item in attrs:
                if hasattr(self, item):
                    dict.update({item: getattr(self, item)})
            return dict

    def reload_from_json(self, json):
        """Reloads attributes from json representation"""
        for key, value in json.items():
            setattr(self, key, value)
