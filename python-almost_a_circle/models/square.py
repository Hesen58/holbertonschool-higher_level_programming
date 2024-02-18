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
        return self.height

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''Something much more useful'''
        zor_list = ["id", "size", "x", "y"]
        if len(args):
            for i in range(len(args)):
                setattr(self, zor_list[i], args[i])
        else:
            for j in kwargs.keys():
                setattr(self, j, kwargs[j])

    def to_dictionary(self):
        '''Something much more usegul'''
        zor_dict = {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
        return zor_dict
