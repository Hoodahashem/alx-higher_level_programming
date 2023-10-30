#!/usr/bin/python3
"""don't give a shit about anything anybody focus on yourself!"""


def print_square(size):
    """
    Print a square with the # character.
    Args: size: The size of the square
    Raises: ValueError and TypeError
    """
    if (not isinstance(size,int)):
        raise TypeError("size must be an integer")
    if (size <= 0):
        raise ValueError("size must be >= 0")
    if (size < 0) and (not isinstance(size,float)):
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#",end="")
        print()