#!/usr/bin/python3
"""
No module imported
"""


class Square:
    """
    class gustavo
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        private instance attribute
        size : gustavo
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        size self
        """
        return self.__size

    @property
    def position(self):
        """position self"""
        return self.__position

    @size.setter
    def size(self, value):
        """
        size
        """
        self.__size = value
        try:
            assert type(value) == int
        except BaseException:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @position.setter
    def position(self, value):
        """position"""
        self.__position = value
        try:
            assert type(value) == tuple
        except BaseException:
            raise TypeError("position must be a tuple of 2 positive integers")
        try:
            assert type(value[0]) == int or type(value[1]) == int
        except BaseException:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """
        gustavo
        """
        return self.__size ** 2

    def my_print(self):
        """Prints"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
