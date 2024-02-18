#!/usr/bin/python3
'''Something useful'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Something more useful'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        zor_name = self.__class__.__name__
        return "[{}] ({}) {}/{} - {}".format(
            zor_name, self.id, self.x, self.y, self.height
        )

    @property
    def size(self):
        return self.__height

    @size.setter
    def size(self, value):
        self.__height = value
        self.__width = value

    def update(self, *args, **kwargs):
        '''Something much more useful'''
        zor_list = ["id", "size", "x", "y"]
        if len(args):
            for i in range(len(args)):
                setattr(self, zor_list[i], args[i])
        else:
            for j in kwargs.keys():
                setattr(self, j, kwargs[j])
