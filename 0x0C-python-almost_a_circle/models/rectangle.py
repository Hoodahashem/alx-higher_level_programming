#!/usr/bin/python3
# rectangle.py
from models.base import Base


"""i'm just working on myself and hoping from GOD that gives me
what i'm looking for."""


class Rectangle(Base):
    """stay hard and let the GOD DO HIS JOB AND JRUST HIM"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new instance of the class"""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        super().__init__(id)

    @property
    def x(self):
        """Returns the x coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the value"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        self.__x = value

    @property
    def y(self):
        """Returns the y coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the value"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        self.__y = value

    @property
    def width(self):
        """Width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the object"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the object"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    def area(self):
        """Returns the area"""
        return self.width * self.height

    def display(self):
        """Display the object"""
        for lol in range(self.y):
            print('\n', end="")
        for i in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Return a string representation of the object"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id,
            self.x,
            self.y,
            self.width,
            self.height
            )
