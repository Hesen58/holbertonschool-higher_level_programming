#!/usr/bin/python3
'''Something useful'''
Base = __import__('7-base_geometry').BaseGeometry


class Rectangle(Base):
    '''Something more useful'''
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width
