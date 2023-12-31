#!/usr/bin/python3
# square.py
"""some documentation"""
from models.rectangle import Rectangle

"""some documentation"""


class Square(Rectangle):
    """Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new instance of the class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """The size of the object"""
        return self.__width

    @size.setter
    def size(self, value):
        """Sets the value for size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """Update the object"""
        if args and len(args) != 0:
            x = 0
            for arg in args:
                if x == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif x == 1:
                    self.size = arg
                elif x == 2:
                    self.x = arg
                elif x == 3:
                    self.y = arg
                x += 1
        elif kwargs and len(kwargs) != 0:
            if 'id' in kwargs:
                if kwargs["id"] is None:
                    self.__init__(self.size, self.x, self.y)
                else:
                    self.id = kwargs["id"]
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """represent the dictionary"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
