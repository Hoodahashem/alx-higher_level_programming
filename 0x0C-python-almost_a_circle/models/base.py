#!/usr/bin/python3
import json
"""i'm just working on myself and hoping from GOD that gives me
what i'm looking for."""


class Base:
    """stay hard and let the GOD DO HIS JOB AND JRUST HIM"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new instance of the class"""
        if id is None:
            self.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
