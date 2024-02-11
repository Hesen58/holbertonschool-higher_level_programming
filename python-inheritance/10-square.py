#!/usr/bin/python3
'''Something useful'''
Rect = __import__('9-rectangle.py').Rectangle


class Square(Rect):
    '''Something more useful'''
    def __init__(self, size):
        super().__init__(size, size)
