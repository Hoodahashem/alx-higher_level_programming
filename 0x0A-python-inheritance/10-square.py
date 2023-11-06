#!/usr/bin/python3

"""some decomentations"""

Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """docstring for Square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
