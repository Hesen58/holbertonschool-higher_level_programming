#!/usr/bin/python3
'''Something useful'''
from models.base import Base


class Rectangle(Base):
    '''Something more useful'''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''Something much more useful'''
        return self.__width * self.__height

    def display(self):
        '''Something much more useful'''
        for j in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        zor_name = self.__class__.__name__
        return "[{}] ({}) {}/{} - {}/{}".format(
            zor_name, self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        '''Something much more useful'''
        zor_list = ["id", "width", "height", "x", "y"]
        if len(args):
            for i in range(len(args)):
                setattr(self, zor_list[i], args[i])
        else:
            for j in kwargs.keys():
                setattr(self, j, kwargs[j])
