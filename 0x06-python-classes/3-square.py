#!/usr/bin/python3

"""
no fucking modules imported!!
"""


class Square:
    """
    there is gustavo in the class
    """

    def __init__(self, size=0):
        """Initialize a new gustavo
            size (int): gustavo int
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """i really hate the coding style"""
        return (self.__size * self.__size)
