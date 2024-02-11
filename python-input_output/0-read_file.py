#!/usr/bin/python3
'''Something useful'''


def read_file(filename=""):
    '''Something more useful'''
    with open("filename", encoding="utf-8") as f:
        zor = f.read()
        return zor
