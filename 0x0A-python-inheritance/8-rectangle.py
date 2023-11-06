#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""some docmentations"""


class Rectangle(BaseGeometry):
    """docstring for Rectangle"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
