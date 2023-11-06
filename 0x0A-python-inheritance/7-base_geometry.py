#!/usr/bin/python3

"""Gus is on the process"""


class BaseGeometry:
    """docstring for BaseGeometry"""
    def area(self):
        """docstring for area"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """docstring for integer_validator"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
