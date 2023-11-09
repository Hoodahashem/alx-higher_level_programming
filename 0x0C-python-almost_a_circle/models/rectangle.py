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
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
