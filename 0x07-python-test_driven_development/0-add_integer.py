#!/usr/bin/python3
"""don't give a shit about anything anybody focus on yourself!"""


def add_integer(a, b=98):
    """
    Return the integer addition of a and b.
    Raises: TypeError
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))