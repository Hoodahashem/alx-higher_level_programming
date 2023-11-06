#!/usr/bin/python3

"""Gus is on the process"""


class BaseGeometry:
    """docstring for BaseGeometry"""
    def area(self):
        """docstring for area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """docstring for integer_validator"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
