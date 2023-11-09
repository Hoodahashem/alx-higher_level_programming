#!/usr/bin/python3

"""i'm just working on myself and hoping from GOD that gives me what i'm looking for."""


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
