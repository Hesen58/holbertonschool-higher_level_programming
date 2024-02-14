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
            zor_name, self.id, self.x, self.y, self.size
        )
