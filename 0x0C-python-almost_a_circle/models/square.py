#!/usr/bin/python3
# rectangle.py
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new instance of the class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """The size of the object"""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the object"""
        if args and len(args)!= 0:
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
                if kwargs["id"] == None:
                    self.__init__(self.size, self.x, self.y)
                else:
                    self.id = kwargs["id"]
            if'size' in kwargs:
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
