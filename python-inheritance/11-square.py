#!/usr/bin/python3
'''Something useful'''
Rect = __import__('9-rectangle').Rectangle


class Square(Rect):
    '''Something more useful'''
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
