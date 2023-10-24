#!/usr/bin/python3

""" def class Square."""


class Square:
    """ this is class square."""
    def __init__(self, size=0):
        """ fucking square class
            size (int): gustavo
        """
        try:
            if type(size) != int:
                raise TypeError
            if size < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
        self.__size = size
