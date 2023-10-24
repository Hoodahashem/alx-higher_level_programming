#!/usr/bin/python3
""" def class Square."""
class Square:
    """ this is class square."""
    def __init__(self, size=0):
        """ fucking square class
            size (int): gustavo
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """
        there is gustavo speaking!
        """
        return self.__size * 2
