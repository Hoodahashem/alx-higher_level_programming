#!/usr/bin/python3

"""there is no fucking modules!"""


class Square:
    """class gustavo"""

    def __init__(self, size=0):
        """Initialize a new gustavo
            size (int): gustavo
        """
        self.size = size

    @property
    def size(self):
        """
        property
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return gustavo"""
        return (self.__size * self.__size)
